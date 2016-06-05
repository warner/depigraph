#!/usr/bin/env python

from setuptools import setup

setup(
    name="depigraph",
    version="0.5.1",
    description="Draw dependency graphs for python distributions",
    author="Brian Warner",
    author_email="warner-depigraph@lothar.com",
    license="MIT",
    url="https://github.com/warner/depigraph",
    py_modules=["depigraph"],
    entry_points={"console_scripts": ["depigraph = depigraph:go"]},
    install_requires=["click"],
    )

# TODO: use pypi 'graphviz' to build the .dot file
