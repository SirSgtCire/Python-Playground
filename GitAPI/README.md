# GitAPI - QA GitMetrics Tool

## Overview

This project enables metric gathering and generation of statistics for code
reviews on Github. It looks in each repository and provides numbers that can be
used to evaluate whether or not sufficient code reviews are being performed.

## Requirements

Requires the following to be installed outside of requirements.txt:
[Python 3](https://docs.python.org/3/), specifically version 3.7.3,
[`pip`](https://pip.pypa.io/en/stable/installing/),
and [venv](https://docs.python.org/3/library/venv.html)

Read the documentation found at venv to better understand its use in this project.
You need to go through the venv documentation before installing this project's
requirements.

## Installation

1. Install all external requirements posted above.
2. Clone the repository
3. Generate your own virtual environment using venv, following the readme for Python-Playground
4. Run the application: `python3 Metrics.py --startdate "[year, month, day]" --enddate "[year, month, day]"`

NOTE: The function uses a `default.json` config file on invoking the code as
listed above. If you want to run the metrics function on a specific set of repos,
then make your own json config file to load and give it as input:
`python3 Metrics.py --cfgfile your_cfg_file.json --startdate "[year, month, day]" --enddate "[year, month, day]"`

## Usage

`appconf.py` is the template file used for loading the variables needed to run
this project. Those variables are loaded into the file from either `default.json`
or from your own custom configuration file that meets your requirements.

When making your own json file, you need to make sure that your variables names
are consistent with what is found in the `appconf.py`. You should only modify the
`appconf.py` itself if you have a clear understanding of the documentation for
using the Github API and how to navigate through its objects. Refer to the given
`default.json` file for help structuring your own configuration file.

`userconf.py` is the user file used for authentication into Github using their API.

When initializing your project, make sure to make your own `userconf.py` with the
following variables:
`username = 'your_github_username'`
`password = 'your_github_password'`
`access_token = 'your_github_access_token'`

If you don't have an access token, then you need to make one on your account that
the authenticator can use. For more info, follow the [online Github documentation](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

## Automation

This module can be run on Jenkins using the jenkins-run.sh provided. If configured correctly, 
Jenkins can handle the scheduled runs of this project, given proper configuration.

Another thing to note is that the Jenkins job takes a `userconf.py` file as one
of its parameters, meaning that after you have created your own file when running
the project locally, you will use that same file to ruin the job. It's important
that each user of this job ensures their Github account is set up properly, with
permission to read all orgs and repos. If that is not the case, then your Github
credentials will not work properly when viewing any orgs and repos outside of
your Github permissions scope.

## API Reference

Uses [Github API V3](https://developer.github.com/v3/)
Requires [github3.py VERSION 0.9.6.](http://github3py.readthedocs.io/en/0.9.6/)
