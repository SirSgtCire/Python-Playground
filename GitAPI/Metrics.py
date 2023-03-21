from functools import reduce
import github3
import csv
import os
import argparse
import userconf
import appconf
import Stats


def __main__():
    # Initialize metrics gathering, then write finalized results to .csv file.
    config, start, end = get_cmd_line_args()
    appconf.load(config, start, end)
    critical_org_metrics, non_critical_org_metrics = run_metrics(Stats.auth(get_credentials()))
    run_csv_writer(critical_org_metrics, non_critical_org_metrics)
    # run_metrics(Stats.auth(get_credentials()))


def get_cmd_line_args():
    parser = argparse.ArgumentParser(description='Parser for loading in config file, the start date and end date.')
    parser.add_argument('--cfgfile', action="store", dest="cfgfile", default="default.json",
                        help="Give the name of a config file you wish to load into the program.")
    parser.add_argument('--startdate', action="store", dest="startdate",
                        help="Give the required start date in the following format: [year, month, day]")
    parser.add_argument('--enddate', action="store", dest="enddate",
                        help="Give the required end date in the following format: [year, month, day]")
    result = parser.parse_args()
    return result.cfgfile, result.startdate, result.enddate


def get_credentials():
    return {'username': userconf.username, 'password': userconf.password, 'access_token': userconf.access_token}


def run_metrics(authed_github):
    critical_org_metrics = []
    non_critical_org_metrics = []

    all_orgs = Stats.get_orgs(authed_github)
    for org in all_orgs:
        print("Organization: {}".format(org.login))
        # critical_org_metrics = []
        # non_critical_org_metrics = []
        critical_repo_metrics = []
        non_critical_repo_metrics = []

        all_repos = Stats.get_repos(authed_github, org)
        for repo in all_repos:
            print("   Repository: {}".format(repo.name))
            if repo.name in appconf.critical_repos_dictionary[org.login]:
                print("   Branch: {}".format(appconf.critical_repos_dictionary[org.login][repo.name]))
                repo_metrics_obj = Stats.calculate_repo_metrics(
                    org, repo, appconf.critical_repos_dictionary[org.login][repo.name])
                critical_repo_metrics.append(repo_metrics_obj)
            else:
                repo_metrics_obj = Stats.calculate_repo_metrics(org, repo, None)
                non_critical_repo_metrics.append(repo_metrics_obj)

        critical_org_metrics.append(Stats.calculate_org_metrics(org, critical_repo_metrics))
        non_critical_org_metrics.append(Stats.calculate_org_metrics(org, non_critical_repo_metrics))

        # run_csv_writer(critical_org_metrics, non_critical_org_metrics)

    return critical_org_metrics, non_critical_org_metrics


def run_csv_writer(critical_org_metrics, non_critical_org_metrics):
    write_dict_list_to_csv(appconf.format_file_name(appconf.get_start_date(),
                           appconf.critical_org_filenames[0], appconf.critical_org_filenames[1]),
                           appconf.org_field_names,
                           csvMetrics(critical_org_metrics))

    write_dict_list_to_csv(appconf.format_file_name(appconf.get_start_date(),
                           appconf.critical_repo_filenames[0], appconf.critical_repo_filenames[1]),
                           appconf.repo_field_names,
                           csvMetrics(reduce(merge_all_repo_lists, critical_org_metrics, [])))

    write_dict_list_to_csv(appconf.format_file_name(appconf.get_start_date(),
                           appconf.non_critical_org_filenames[0], appconf.non_critical_org_filenames[1]),
                           appconf.org_field_names,
                           csvMetrics(non_critical_org_metrics))

    write_dict_list_to_csv(appconf.format_file_name(appconf.get_start_date(),
                           appconf.non_critical_repo_filenames[0], appconf.non_critical_repo_filenames[1]),
                           appconf.repo_field_names,
                           csvMetrics(reduce(merge_all_repo_lists, non_critical_org_metrics, [])))


def csvMetrics(metrics):
    return map(lambda m: m.serialize(), metrics)


def merge_all_repo_lists(acc, org_obj):
    return (acc + org_obj.repo_metrics)


def write_dict_list_to_csv(filename, headers, metrics_list):
    file_exists = os.path.isfile(filename)

    with open(filename, 'w') as csvfile:
    # with open(filename, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        for metrics_item in metrics_list:
            writer.writerow(metrics_item)


if __name__ == "__main__":
    __main__()
