from collections import namedtuple


ORG_METRIC_FIELDS = ['name', 'num_commits', 'num_pull_requests', 'num_associated_commits',
                     'num_unassociated_commits', 'repo_metrics']


class OrgMetrics(namedtuple('_OrgMetrics', ORG_METRIC_FIELDS)):
    # Creates a .csv writable dict.
    def serialize(self):
        return {
            'Organization': self.name,
            'Total Pull Requests': self.num_pull_requests,
            'Total Associated Commits': self.num_associated_commits,
            'Total Unassociated Commits': self.num_unassociated_commits,
            'Total Overall Commits': self.num_commits}


REPO_METRIC_FIELDS = ['org', 'name', 'branch', 'is_critical', 'num_commits', 'num_pull_requests',
                      'num_associated_commits', 'num_unassociated_commits', 'unassociated_ids']


class RepoMetrics(namedtuple('_RepoMetrics', REPO_METRIC_FIELDS)):
    # Creates a .csv writable dict.
    def serialize(self):
        return {
            'Organization': self.org,
            'Repository': self.name,
            'Branch': self.branch,
            'Critical': self.is_critical,
            'Pull Requests': self.num_pull_requests,
            'Associated Commits': self.num_associated_commits,
            'Unassociated Commits': self.num_unassociated_commits,
            'Total Commits': self.num_commits,
            'Commit IDs': self.unassociated_ids}


class PullRequestSummary(object):
    def __init__(self, shas, counter):
        self.relevance_counter = counter
        self.relevant_commit_shas = shas


class CommitSummary(object):
    def __init__(self, sha, associated):
        self.associated = associated
        self.sha = sha
