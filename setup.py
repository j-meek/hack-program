#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# build command
setup(
    name="juniper",
    version="0.0.1",
    author="Jared Meek",
    packages=["juniper"],
    entry_points={
        'console_scripts': ['juniper = juniper.__main__:main']
    }
)
