#!/bin/python2.7
# -*- coding: utf-8 -*-
"""
Jakub Janarek 2018
"""

import sys
import os
import codecs


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


packages = [
    'newspaper',
]


if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist upload -r pypi')
    sys.exit()


# This *must* run early. Please see this API limitation on our users:
# https://github.com/codelucas/newspaper/issues/155
if sys.version_info[0] == 2 and sys.argv[-1] not in ['publish', 'upload']:
    sys.exit('WARNING! You are attempting to install newspaper3k\'s '
             'python3 repository on python2. PLEASE RUN '
             '`$ pip3 install newspaper3k` for python3 or '
             '`$ pip install newspaper` for python2')


with open('requirements.txt') as f:
    required = f.read().splitlines()


with codecs.open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()


setup(
    name='newspaper_no_download',
    version='0.0.1',
    description='Newspaper3k library with no download phase',
    long_description=readme,
    author='Jakub Janarek',
    author_email='jjanarek@gmail.com',
    url='https://github.com/jxub/newspaper_no_download',
    packages=packages,
    include_package_data=True,
    install_requires=required,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Intended Audience :: Developers',
    ],
)
