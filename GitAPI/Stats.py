from functools import reduce, partial
import github3
import datetime
import uritemplate
import appconf
import Models


def auth(auth_dict):
    # If we are given a relevant organizations list (a focus group, if you
    # will), then we only need to use the front part of the base url, and in
    # fact will not work properly with github3 given the full organizations url.
    if appconf.critical_repos_dictionary:
        return github3.login(auth_dict['username'], auth_dict['password'],
                             auth_dict['access_token'], appconf.api_call_relevant)
    else:
        return github3.login(auth_dict['username'], auth_dict['password'],
                             auth_dict['access_token'], appconf.api_call_base)


def get_orgs(gh_obj):
    # Check the given relevant organizations list in appconf to decide
    # which organizations to gather metrics on.
    if appconf.critical_repos_dictionary:
        initialized_orgs = []
        for rel_org in appconf.critical_repos_dictionary.keys():
            initialized_orgs.append(gh_obj.organization(rel_org))
        return initialized_orgs
    else:
        return list(gh_obj.iter_orgs())


def get_repos(gh_obj, org):
    return list(org.iter_repos())


def calculate_org_metrics(org, repo_metrics):
    (num_commits, num_pull_requests, num_associated_commits, num_unassociated_commits) = \
        reduce(merge_org_metrics, repo_metrics, (0, 0, 0, 0))

    return Models.OrgMetrics(
        name=org.login,
        num_commits=num_commits,
        num_pull_requests=num_pull_requests,
        num_associated_commits=num_associated_commits,
        num_unassociated_commits=num_unassociated_commits,
        repo_metrics=repo_metrics)


def merge_org_metrics(acc, repo_obj):
    return(
        acc[0] + repo_obj.num_commits,
        acc[1] + repo_obj.num_pull_requests,
        acc[2] + repo_obj.num_associated_commits,
        acc[3] + repo_obj.num_unassociated_commits)


def calculate_repo_metrics(org, repo, branch):
    try:
        pr_summaries = get_pull_request_summaries(repo)
        prs_to_count, rel_commit_shas = reduce(merge_pr_summary_tuples, pr_summaries, (0, []))
        print("      Pull request summaries have been collected.")

        commit_summaries = get_commit_summaries(repo, branch, rel_commit_shas)
        num_commits = len(list(commit_summaries))
        unassociated_commits = irrelevant_files_filter(
            repo, list(filter(lambda c: not c.associated, commit_summaries)))
        unassociated_ids = list(map(lambda c: c.sha, unassociated_commits))
        num_unassociated_commits = len(list(unassociated_commits))
        num_associated_commits = num_commits - num_unassociated_commits
        print("      Commit summaries have been collected.")

        return Models.RepoMetrics(
            org=org.login,
            name=repo.name,
            branch=branch,
            is_critical=repo.name in appconf.critical_repos_dictionary[org.login],
            num_commits=num_commits,
            num_pull_requests=prs_to_count,
            num_associated_commits=num_associated_commits,
            num_unassociated_commits=num_unassociated_commits,
            unassociated_ids=unassociated_ids)

    # Handle github3 409 empty repository error thrown by uninitialized repositories,
    # and log this error in the commit ids column in the .csv file.
    except github3.models.GitHubError as gh_err:
        commit_detail = "github3.models.GitHubError: {0}".format(gh_err).encode('UTF8')

        return Models.RepoMetrics(
            org=org.login,
            name=repo.name,
            branch="None",
            is_critical=False,
            num_commits=0,
            num_pull_requests=0,
            num_associated_commits=0,
            num_unassociated_commits=0,
            unassociated_ids=commit_detail)


def merge_pr_summary_tuples(acc, summary):
    if acc is not None and summary is not None:
        return (acc[0] + summary.relevance_counter, acc[1] + summary.relevant_commit_shas)
    else:
        return (acc[0] + 0, acc[1] + [])


def get_pull_request_summaries(repo):
    return list(map(summarize_pull_request, repo.iter_pulls(state='closed')))


def summarize_pull_request(pull):
    shas = []

    if pull.is_merged() and pull.merged_at > appconf.get_start_date() and pull.merged_at < appconf.get_end_date():
        # We only want to evaluate pull requests within the given time period.
        if pull.merge_commit_sha is not None and pull.merge_commit_sha not in shas:
            shas.append(pull.merge_commit_sha)

        if pull.head.sha is not None and pull.head.sha not in shas:
            shas.append(pull.head.sha)

        for commit in pull.iter_commits():
            shas.append(commit.sha)
        # Pull requests in the given time period are given the value 1 so we count them.
        return Models.PullRequestSummary(shas, counter=1)
    else:
        return Models.PullRequestSummary(shas, counter=0)


def irrelevant_files_filter(repo, commits_list):
    # A function that filters out versioning commits and readme commits, which have both been
    # considered irrelevant for the purposes of code reviews and will no longer be tracked.
    updated_commits_list = []
    for commit in commits_list:
        for commit_file in repo.commit(commit.sha).files:
            if all(filename not in commit_file["filename"] for filename in appconf.irrelevant_files_list):
                if commit not in updated_commits_list:
                    updated_commits_list.append(commit)
    return updated_commits_list


def get_commit_summaries(repo, branch, rel_commit_shas):
    if branch is not None:
        return list(map(partial(summarize_commit, rel_commit_shas=rel_commit_shas), repo.iter_commits(
            sha=branch, since=appconf.get_start_date().isoformat(), until=appconf.get_end_date().isoformat())))
    else:
        return list(map(partial(summarize_commit, rel_commit_shas=rel_commit_shas), repo.iter_commits(
            sha='master', since=appconf.get_start_date().isoformat(), until=appconf.get_end_date().isoformat())))


def summarize_commit(commit, rel_commit_shas):
    commit_sha = (commit.commit.sha.encode('UTF8')).decode('UTF8')

    if commit.sha in rel_commit_shas or commit.commit.committer['name'] in appconf.automated_users_list:
        return Models.CommitSummary(commit_sha, associated=True)
    else:
        return Models.CommitSummary(commit_sha, associated=False)
