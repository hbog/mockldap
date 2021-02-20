#!/usr/bin/env python3

from setuptools import setup


def readall(path):
    with open(path) as fp:
        return fp.read()


setup(
    name='mockldap',
    version='0.3.0.post1',
    description="A simple mock implementation of python-ldap.",
    url='https://github.com/psagers/mockldap',
    project_urls={
        'Documentation': 'https://mockldap.readthedocs.io/',
    },
    author='Peter Sagerson',
    author_email='psagers@ignorare.net',
    license='CC0-1.0',
    packages=['mockldap'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP',
    ],
    keywords=['mock', 'ldap'],
    install_requires=[
        'funcparserlib == 0.3.6',
        'mock; python_version < "3.0"',
        'python-ldap >= 3.0',
    ],
    setup_requires=[
        'setuptools >= 0.6c11',
    ],
    test_suite='tests',
)
