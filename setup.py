"""
    setup.py - Pyappi setup file
"""

from __future__ import print_function
from setuptools import Command, setup

setup(
    name='Pyappi',
    version='0.1-dev',
    url='http://github.com/yyyar/pyappi',
    license='BSD',
    author='Yaroslav Pogrebnyak',
    author_email='yyyaroslav@gmail.com',
    description='A library for building declarative REST APIs on top of popular web frameworks',
    long_description=__doc__,
    packages=['pyappi'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)