# Python-Playground
Fun environment for throwing Python code at the wall.

# Setting up Environments
0. navigate to root of Python-Playground
1. create virtual environment: `python3 -m venv Venvs/<name_of_module>`
2. run `source Venvs/<name_of_module>/bin/activate` to enable new venv
3. upgrade pip and setup tools: `pip install -U pip setuptools`
4. install module dependencies: `pip install -r <name_of_module>/requirements.txt`
5. when done using venv, run `deactivate`
6. to reset packages without deleting venv, run `pip uninstall -r <(grep -v -f requirements.txt <(pip freeze))`

# Using the Modules
TBD when in place
