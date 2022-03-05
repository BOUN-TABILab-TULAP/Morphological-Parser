#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools
from distutils.spawn import find_executable
import os
from setuptools.command.install import install
import subprocess

with open("README.md", "r") as f:
    long_description = f.read()

with open(os.path.join("morphological_parser", "version.txt"), "r") as f:
    __version__ = f.read().strip()


setuptools.setup(
    name="morphological_parser",
    version=__version__,
    author="Haşim Sak",
    author_email="tabilab.dip@gmail.com",
    description="Morphological Parser and Disambiguator with Python Bindings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tabilab-dip/morphological_parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux",
    ],
    package_data={
        "morphological_parser": [
            "model.txt",
            "turkish.fst",
            "TurkishMorphology.so"
        ]
    },
    exclude_package_data={ # we don't need api for packaged application
        "morphological_parser": [
            "api.py",
        ]
    },
    install_requires=[], # no requirements, flask is needed for server
    python_requires='>=3.6',
)
