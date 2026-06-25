#!/bin/bash -ex
# Naming the virtual environment for gitmetrics
MY_VENV=gitmetrics-venv
# Create the virtual environment if it does not exist already
echo "Building venv" && \
scl enable rh-python36 "test -d $MY_VENV || virtualenv -q $MY_VENV"
# Activate the virtual environment
# optional step - you can upgrade pip, setuptools etc. And if you do so ALWAYS use an explicit version
# and last install the dependencies as specified in the requirement file
echo "Activating venv and installing requirements" && \
source $MY_VENV/bin/activate && \
pip install --upgrade pip==20.0.2 && \
pip install -r requirements.txt
# Gather the github metrics
python Metrics.py --cfgfile "${cfgfile}" --startdate "${startdate}" --enddate "${enddate}"
