# ++++++++ set up a Project +++++++++++++++++ #
# 1 Install packages.
# pip check <---- it came with python, but needs to be upgrated, done.
# distribute check
# nose check
# virtualenv check

# +++++++++ create directory for the skeleton project ++++++++ #
# in shell, type:
'''
$ mkdir projects
$ cd projects
$ mkdir skeleton
$ cd skeleton
$ mkdir bin NAME tests docs
'''
# The directory NAME will be renamed to whatever you are calling your project's main module when you use the skeleton.

# set up the init files:
'''
$ touch NAME/__init__.py
$ touch tests/__init__.py
'''

# create an empty Python module directories we can put our code in.
#then we need to create a setup.py file we can use to install our porject later if we want:
