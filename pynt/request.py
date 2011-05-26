#!/usr/bin/python

from httplib2 import Http
from urllib import quote, urlencode
from urllib2 import HTTPError
from settings import API_URL, PUBLIC_TOKEN, PRIVATE_TOKEN

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


class Request(object):

	def __init__(self):
		"""
			Instantiates an instance of Request
		"""
		# Get a client for making requests
		self.client = Http()

	# Handle GET requests
	def get(self, url, params={}):
		# Add the public token to the parameters
		params['token'] = PUBLIC_TOKEN

		# dict to query string from: http://bit.ly/k1fAsx
		query_string = '&'.join([k+'='+quote(str(v)) for (k,v) in params.items()])
	
		# Mash it all together and send it off!
		url = "%s%s?%s" % (API_URL, url, query_string,)
		resp, content = self.client.request(url, 'GET')
	
		# TODO: If resp != 200, what do we do?
		return simplejson.loads(content)

	# Handle POST requests	
	def post(self, url, params={}):
		# Add the private token to the parameters
		params['token'] = PRIVATE_TOKEN

		url = "%s%s" % (API_URL, url,)
		body = simplejson.dumps(params)
		headers = {'Content-Type': 'application/json'}
	
		resp, content = self.client.request(url, 'POST', body=body, headers=headers)
	
		if resp['status'] == 201:
			return resp['location']
		else:
			return "Http Error Code: %s\nResponse: %s" % (resp['status'], content,)
		
	# Handle DELETE requests	
	def delete(self, url):
		# Add the private token to the parameters
		params = {'token': PRIVATE_TOKEN}

		url = "%s%s" % (API_URL, url,)
		body = simplejson.dumps(params)
		headers = {'Content-Type': 'application/json'}
	
		resp, content = self.client.request(url, 'DELETE', body=body, headers=headers)
	
		if resp['status'] == '200':
			return 1
		else:
			return "Http Error Code: %s\nResponse: %s" % (resp['status'], content,)
		
