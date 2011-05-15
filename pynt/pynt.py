#!/usr/bin/python

"""
	Pynt is a Python client that wraps the Open Beer Database API.

	Questions, comments? m@h0ke.com
"""

__author__ = "Matthew Hokanson <m@h0ke.com>"
__version__ = "0.1.0"

from httplib2 import Http
from urllib import quote
from urllib2 import HTTPError

# Attempt to import simplejson (not so simple, huh?)
try:
	# Python 2.6 and up
	import json as simplejson
except ImportError:
	try:
		# Python 2.6 and lower
		import simplejson
	except:
		# Rut roh.
		raise Exception("simplejson (or Python 2.6 and higher) is required")

# Set the API's URL
API_URL = 'http://api.openbeerdatabase.com/v1/'



class Pynt(object):
	def __init__(self, public_token = None, private_token = None):
		"""
		    Instantiates an instance of Pynt.

			Parameters:
				public_token - Given to you when you register.
				private_token - Given to you when you register.
		"""
		# Set the tokens
		self.public_token = public_token
		self.private_token = private_token

	    # Get a client for making requests
		self.client = Http()
		
	# Handle GET requests
	def get(self, url, options={}):
		# dict to query string from: http://bit.ly/k1fAsx
		query_string = '&'.join([k+'='+quote(str(v)) for (k,v) in options.items()])
		
		# Mash it all together and send it off!
		url = "%s%s?%s" % (API_URL, url, query_string)
		resp, content = self.client.request(url, 'GET')
		
		# TODO: If resp != 200, what do we do?
		return simplejson.loads(content)
		
	#TODO: def post() -- http://code.google.com/p/httplib2/wiki/Examples
		

	#
	# BEERS
	#	
	
	# Get list of all beers
	def get_beers(self, **kwargs):
		return self.get("beers.json", kwargs)
		
	# Get beer by id
	def get_beer(self, id):
		return self.get("beers/%d.json" % (id,))
		
	#
	# BREWERIES
	#
		
	# Get list of all breweries
	def get_breweries(self, **kwargs):
		return self.get("breweries.json", kwargs)
		
	# Get brewery by id
	def get_brewery(self, id):
		return self.get("breweries/%d.json" % (id,))
		
