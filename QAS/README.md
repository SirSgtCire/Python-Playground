# Quality Assurance Strategies

## Overview



## Installation and Usage

1. Install all external requirements posted above.
2. Clone the repository and [install requirements](https://github.com/SirSgtCire/Python-Playground/blob/develop/QAS/requirements.txt)
3. Generate your own virtual environment using venv, following the readme for Python-Playground
4. Run the application: `python3 QAS/main.py"`

NOTE: The function uses a `default.json` config file on invoking the code as
listed above. If you want to run the metrics function on a specific set of repos,
then make your own json config file to load and give it as input:
`python3 QAS/main.py --cfgfile your_cfg_file.json"`
