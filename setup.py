#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_packages


def readme():
    with open('README.txt') as f:
        return f.read()


install_requires = ['requests']
if sys.version[:3] < '3.4':
    install_requires.append('pathlib')
if sys.version[:3] < '3.3':
    install_requires.append('mock')

setup(
        packages=find_packages(exclude=['tests', 'tests.*']),
        name='httpath',
        version='0.1',
        author='João Santos',
        author_email='jmcs@jsantos.eu',
        url='https://github.com/jmcs/httpath',
        description="Object-oriented HTTP from `urllib.parse`, `pathlib` and `requests`",
        long_description=readme(),
        classifiers=['Development Status :: 5 - Production/Stable',
                     'Environment :: Web Environment',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: Python Software Foundation License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python :: 3.4',
                     'Topic :: Internet :: WWW/HTTP',
                     'Topic :: Software Development :: Libraries :: Python Modules'],
        license='PSF',
        install_requires=install_requires,
)
