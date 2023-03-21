print("""
Welcome to GitAPI!

This project enables metric gathering and generation of statistics for code
reviews on Github. It looks in each repository and provides numbers that can be
used to evaluate whether or not sufficient code reviews are being performed.

Read the documentation found at venv to better understand its use in this project.
You need to go through the venv documentation before installing this project's
requirements.

`appconf.py` is the template file used for loading the variables needed to run
this project.

`userconf.py` is the user file used for authentication into Github using their API.

If you don't have an access token, then you need to make one on your account that
the authenticator can use.
""")