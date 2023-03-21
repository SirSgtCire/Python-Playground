import github3
import csv
import userconf
import json
import datetime
import pytz
import uritemplate
from functools import partial
from collections import namedtuple


"""
The below class is how we store the collected data efficiently, to eventually write to a csv file.
"""
PULL_COMMENT_FIELDS = [
    'org_login', 'repo_name', 'pull_title', 'pull_body', 'pull_status',
    'comment_body', 'comment_submitter', 'comment_created_at'
]


class PullCommentMetaData(namedtuple('_PullCommentMetaData', PULL_COMMENT_FIELDS)):
    def serialize(self):
        return {
            'Organization': self.org_login,
            'Repository': self.repo_name,
            'Pull Request ID': self.pull_title,
            'Pull Request Body': self.pull_body,
            'Pull Request Status': self.pull_status,
            'Comment Body': self.comment_body,
            'Comment Submitter': self.comment_submitter,
            'Date Created': self.comment_created_at
        }


"""
The below functions are used to iterate over pull requests and gather relevant data.
"""
def get_credentials():
    return {
            'username': userconf.username,
            'password': userconf.password,
            'access_token': userconf.access_token
    }


def auth(auth_dict):
    return github3.login(auth_dict['username'], auth_dict['password'],
                         auth_dict['access_token'], api_call_relevant)


def get_orgs(gh_obj):
    if relevant_repos_dictionary:
        initialized_orgs = []
        for rel_org in relevant_repos_dictionary.keys():
            initialized_orgs.append(gh_obj.organization(rel_org))
        return initialized_orgs
    else:
        return list(gh_obj.iter_orgs())


def get_repos(gh_obj, org):
    if relevant_repos_dictionary:
        return list(org.iter_repos())


def get_closed_pulls(repo):
    # NOTE: The status of merged in Github is bugged and can't be called upon through the API,
    # so if a pull request is merged, but not closed, then it may not show up in this list
    # until that pull request is closed. However, after a timed delay, merged pull Requests
    # do automatically close themselves, as can be seen under the pull requests tab in any repo.
    initialized_pulls = []
    for pull in repo.iter_pulls(state='closed'):
        if pull.closed_at > start_date and pull.closed_at < end_date:
            initialized_pulls.append(pull)
    return initialized_pulls


def get_review_comments(org, repo, pull):
    # The following loop looks at comments directly on the pull request.
    review_comment_id_list = []
    review_comment_list = []
    for review_comment in pull.iter_comments():
        if review_comment.id not in review_comment_id_list:
            review_comment_list.append(store_pull_comment_metadata(org, repo, pull, review_comment))
            review_comment_id_list.append(review_comment.id)
    return review_comment_list


def get_issue_comments(org, repo, pull):
    # The following loop looks at comments on issues associated with the pull request.
    issue_comment_id_list = []
    issue_comment_list = []
    for issue_comment in pull.iter_issue_comments():
        if issue_comment.id not in issue_comment_id_list:
            issue_comment_list.append(store_pull_comment_metadata(org, repo, pull, issue_comment))
            issue_comment_id_list.append(issue_comment.id)
    return issue_comment_list


def get_pull_comment_metadata(authed_github):
    pull_comment_metadata = []

    all_orgs = get_orgs(authed_github)
    for org in all_orgs:
        all_repos = get_repos(authed_github, org)
        for repo in all_repos:
            if repo.name in relevant_repos_dictionary[org.login]:
                all_pulls = get_closed_pulls(repo)
                for pull in all_pulls:
                    pull_comment_metadata.extend(get_review_comments(org, repo, pull))
                    pull_comment_metadata.extend(get_issue_comments(org, repo, pull))
    return pull_comment_metadata


def store_pull_comment_metadata(org, repo, pull, comment):
    return PullCommentMetaData(
        org_login=org.login,
        repo_name=repo.name,
        pull_title=pull.title.encode("utf-8"),
        pull_body=pull.body.encode("utf-8"),
        pull_status=pull.state,
        comment_body=comment.body.encode("utf-8"),
        comment_submitter=comment.user,
        comment_created_at=comment.created_at)


def format_file_name(date, node_type, subject_matter):
    return "{0.year}_{0.month}_{1}_{2}.csv".format(date, node_type, subject_matter)


def csvMetrics(metrics):
    return map(lambda m: m.serialize(), metrics)


def write_data_to_csv(filename, headers, metrics_list):
    with open(filename, 'wb') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for metrics_item in metrics_list:
            writer.writerow(metrics_item)


"""
The below data contains configurations needed to run the script.
"""
start_date = datetime.datetime(2017, 7, 1, 0, 0, 0, 0, pytz.UTC)
end_date = datetime.datetime(2017, 7, 31, 23, 59, 59, 999999, pytz.UTC)
api_call_relevant = 'https://github.rp-core.com'
pull_comment_file_name = format_file_name(start_date, "pull_comment", "contributions_summary")
pull_comment_field_names = [
    'Organization', 'Repository', 'Pull Request ID', 'Pull Request Body',
    'Pull Request Status', 'Comment Body', 'Comment Submitter', 'Date Created'
]
relevant_repos_dictionary = {
    'OD': [
        'adengine',
        'scheduler',
        'rts',
        'pacemaker',
        'metrics',
        'ae-mrfs',
        'jira-git-integration-test',
        'java_matchmaker',
        'ae-trunk-tools',
    ],
}


"""
The below function is our main function, which, for formality sake, could be moved to its own file.
"""
def __main__():
    write_data_to_csv(
        pull_comment_file_name,
        pull_comment_field_names,
        csvMetrics(get_pull_comment_metadata(auth(get_credentials())))
    )


if __name__ == "__main__":
    __main__()
