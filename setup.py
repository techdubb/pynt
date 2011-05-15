#!/usr/bin/python

import sys, os
from setuptools import setup
from setuptools import find_packages

__author__ = 'Matthew Hokanson <m@h0ke.com>'
__version__ = '0.1.0'

setup(
	name = 'pynt',
	version = __version__,
	
	install_requires = ['simplejson', 'httplib2'],

	author = 'Matthew Hokanson',
	author_email = 'm@h0ke.com',
	license = 'MIT License',
	url = 'http://github.com/h0ke/pynt/tree/master',
	keywords = 'open beer database python wrapper pynt',
	description = 'Pynt is a Python client that wraps the Open Beer Database API.',
	long_description = open('README.markdown').read(),
	classifiers = [
		'Development Status :: 1 - Planning',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Internet'
	]
)
