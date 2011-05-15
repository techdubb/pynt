#!/usr/bin/python

"""
	Pynt is a library for Python that wraps the Open Beer Database API.

	Questions, comments? m@h0ke.com
"""

__author__ = "Matthew Hokanson <m@h0ke.com>"
__version__ = "0.1"

import urllib
import urllib2
import urlparse
import httplib
import httplib2
import re

# Pynt maps keyword based arguments to OBDB API endpoints. The endpoints
# table is a file with a dictionary of every API endpoint that Pynt supports.
from obdb_endpoints import base_url, api_table

from urllib2 import HTTPError

# There are some special setups (like, oh, a Django application) where
# simplejson exists behind the scenes anyway. Past Python 2.6, this should
# never really cause any problems to begin with.
try:
	# Python 2.6 and up
	import json as simplejson
except ImportError:
	try:
		# Python 2.6 and below (2.4/2.5, 2.3 is not guranteed to work with this library to begin with)
		import simplejson
	except ImportError:
		try:
			# This case gets rarer by the day, but if we need to, we can pull it from Django provided it's there.
			from django.utils import simplejson
		except:
			# Rut roh.
			raise Exception("Pynt requires the simplejson library (or Python 2.6) to work. http://www.undefined.org/python/")

class PyntError(AttributeError):
	"""
		Generic error class, catch-all for most Pynt issues.
		Special cases are handled by APILimit and AuthError.

		Note: To catch these, you need to explicitly import them into your code, e.g:

		from pynt import PyntError, APILimit, AuthError
	"""
	def __init__(self, msg, error_code=None):
		self.msg = msg
		if error_code == 400:
			raise APILimit(msg)

	def __str__(self):
		return repr(self.msg)


class APILimit(PyntError):
	"""
		Raised when you've hit an API limit. 
	"""
	def __init__(self, msg):
		self.msg = msg

	def __str__(self):
		return repr(self.msg)


class AuthError(PyntError):
	"""
		Raised when you try to access a protected resource and it fails due to some issue with
		your authentication.
	"""
	def __init__(self, msg):
		self.msg = msg

	def __str__(self):
		return repr(self.msg)


class Pynt(object):
	def __init__(self, public_token = None, private_token = None, headers=None, callback_url=None, client_args={}):
		"""
		    Instantiates an instance of Pynt. Takes optional parameters for authentication and such (see below).

			Parameters:
				public_token - Given to you when you register your application with OBDB.
				private_token - Given to you when you register your application with OBDB.
				headers - User agent header, dictionary style ala {'User-Agent': 'Bert'}
				client_args - additional arguments for HTTP client (see httplib2.Http.__init__), e.g. {'timeout': 10.0}
		"""
		# Needed for hitting that there API.
		self.public_token = public_token
		self.private_token = private_token

		# If there's headers, set them, otherwise be an embarassing parent for their own good.
		self.headers = headers
		if self.headers is None:
			self.headers = {'User-agent': 'Pynt - Python Open Beer Database Library v1'}
			
	    # If they don't do authentication, but still want to request unprotected resources, we need an opener.
		self.client = httplib2.Http(**client_args)

	def __getattr__(self, api_call):
		"""
			FYI, Python classes have this great feature known as __getattr__().
			
			It's called when an attribute that was called on an object doesn't seem to exist - since it doesn't exist,
			we can take over and find the API method in our table. We then return a function that downloads and parses
			what we're looking for, based on the keywords passed in.
		"""
		def get(self, **kwargs):
			# Go through and replace any mustaches that are in our API url.
			fn = api_table[api_call]
			base = re.sub(
				'\{\{(?P<m>[a-zA-Z_]+)\}\}',
				lambda m: "%s" % kwargs.get(m.group(1), '1'), # The '1' here catches the API version.
				base_url + fn['url']
			)

			# Then open and load
			if fn['method'] == 'POST':
				resp, content = self.client.request(base, fn['method'], urllib.urlencode(dict([k, Pynt.encode(v)] for k, v in kwargs.items())), headers = self.headers)
			else:
				url = base + "?" + "&".join(["%s=%s" %(key, value) for (key, value) in kwargs.iteritems()])
				resp, content = self.client.request(url, fn['method'], headers = self.headers)

			return simplejson.loads(content)

		if api_call in api_table:
			return get.__get__(self)
		else:
			raise PyntError, api_call
			
	@staticmethod
	def unicode2utf8(text):
		try:
			if isinstance(text, unicode):
				text = text.encode('utf-8')
		except:
			pass
		return text

	@staticmethod
	def encode(text):
		if isinstance(text, (str,unicode)):
			return Pynt.unicode2utf8(text)
		return str(text)
