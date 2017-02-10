try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project: redrock',
    'author': 'Miaojun Zhang',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'mzhang56@horizon.csueastbay.edu',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['redrock_project_name'],
    'scripts': [],
    'name': 'redrock_project'
}

setup(**config) # <----- what is it????
