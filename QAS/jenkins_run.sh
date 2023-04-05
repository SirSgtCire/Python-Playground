#!/bin/bash -ex

[[ ! -e ${WORKSPACE}/vmb-qa-venv ]] && echo "Building venv" && \
/opt/rh/rh-python36/root/usr/bin/python3 -m venv vmb-qa-venv
source ${WORKSPACE}/vmb-qa-venv/bin/activate && \
pip install -r requirements.txt

echo -e "Activating venv"
source ${WORKSPACE}/vmb-qa-venv/bin/activate

# cp command to get userconf.py into working directory.

pytest -s test_vmb.py --junitxml=testng-results.xml
