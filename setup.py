#!/usr/bin/python

import sys, os
from setuptools import setup
from setuptools import find_packages

__author__ = 'Matthew Hokanson <m@h0ke.com>'
__version__ = '0.1'

setup(
	# Basic package information.
	name = 'pynt',
	version = __version__,
	packages = find_packages(),

	# Packaging options.
	include_package_data = True,

	# Package dependencies.
	install_requires = ['simplejson', 'httplib2'],

	# Metadata for PyPI.
	author = 'Matthew Hokanson',
	author_email = 'm@h0ke.com',
	license = 'MIT License',
	url = 'http://github.com/h0ke/pynt/tree/master',
	keywords = 'open beer database python wrapper pynt',
	description = 'An easy way to access the Open Beer Database with Python.',
	long_description = open('README.markdown').read(),
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Internet'
	]
)
