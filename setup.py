#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from pathlib import Path
from setuptools import setup


ROOT_PATH = Path(__file__).parent

LICENSE_PATH = ROOT_PATH / 'LICENSE'

README_PATH = ROOT_PATH / 'README.md'

REQUIREMENTS_PATH = ROOT_PATH / 'requirements.txt'

REQUIREMENTS_TEST_PATH = ROOT_PATH / 'requirements_dev.txt'


def stream_requirements(fd):
    """For a given requirements file descriptor, generate lines of
    distribution requirements, ignoring comments and chained requirement
    files.
    """
    for line in fd:
        cleaned = re.sub(r'#.*$', '', line).strip()
        if cleaned and not cleaned.startswith('-r'):
            yield cleaned


with REQUIREMENTS_PATH.open() as requirements_file:
    REQUIREMENTS = list(stream_requirements(requirements_file))


with REQUIREMENTS_TEST_PATH.open() as test_requirements_file:
    REQUIREMENTS_TEST = REQUIREMENTS[:]
    REQUIREMENTS_TEST.extend(stream_requirements(test_requirements_file))


setup(
    name='results_schema',
    version='1.2.1',
    description="Store results of modeling runs",
    long_description=README_PATH.read_text(),
    author="Center for Data Science and Public Policy",
    author_email='datascifellows@gmail.com',
    url='https://github.com/dssg/results-schema',
    packages=[
        'results_schema',
        'results_schema.alembic',
        'results_schema.alembic.versions',
    ],
    include_package_data=True,
    install_requires=REQUIREMENTS,
    tests_require=REQUIREMENTS_TEST,
    license=LICENSE_PATH.read_text(),
    zip_safe=False,
    keywords='analytics datascience modeling modelevaluation',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ]
)
