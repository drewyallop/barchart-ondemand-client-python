#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from os import path
import io

here = path.abspath(path.dirname(__file__))

NAME = 'barchart'
with io.open(path.join(here, NAME, 'version.py'), 'rt', encoding='UTF-8') as f:
    exec(f.read())

setup(
    name=NAME,
    version=__version__,
    description='A Python library to get data from BarChart API',
    long_description='README.rst',
    url=__url__,
    author=__author__,
    author_email=__email__,
    license=__license__,

    classifiers=[
        'Development Status :: 4 - Beta',

        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',

        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',

        'License :: OSI Approved :: MIT License',
    ],

    keywords='python trading data interface',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
    extras_require={
        'dev': ['check-manifest', 'nose'],
        'test': ['coverage', 'nose'],
    },

    package_data={
        'samples': ['samples/*.py'],
    },
)
