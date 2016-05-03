#!/usr/bin/env python

from setuptools import setup

import versioneer

setup_args = {
    'name': "depigraph",
    'version': versioneer.get_version(),
    'description': "Draw dependency graphs of Python distributions",
    'author': "Brian Warner",
    'author_email': "warner-depigraph@lothar.com",
    'url': "https://github.com/warner/depigraph",
    'license': "MIT",
    'long_description': """\
Draw dependency graphs of Python distributions.
""",
    'classifiers': [
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: System :: Distributed Computing",
        "Topic :: Software Development",
        ],
    'platforms': ["any"],

    'scripts': ["depigraph"],

    'cmdclass': versioneer.get_cmdclass(),
}


setup(**setup_args)
