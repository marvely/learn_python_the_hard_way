try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project: exer47',
    'author': 'Miaojun Zhang',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'mzhang56@horizon.csueastbay.edu',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['exer47'],
    'scripts': [],
    'name': 'exer47'
}

setup(**config) # <----- what is it????
