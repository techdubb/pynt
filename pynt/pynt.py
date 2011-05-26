#!/usr/bin/python

"""
	Pynt is a Python client that wraps the Open Beer Database API.

	Questions, comments? m@h0ke.com
"""

__author__ = "Matthew Hokanson <m@h0ke.com>"
__version__ = "0.1.0"


from request import Request


class Pynt(object):

	def __init__(self):
		"""
			Instantiates an instance of Pynt
		"""
		
		# Instantiate Request object
		self.r = Request()
		
		
	# BEERS
	
	# Get list of all beers
	def get_beers(self, **kwargs):
		return self.r.get("beers.json", kwargs)
		
	# Get beer by id
	def get_beer(self, id):
		return self.r.get("beers/%d.json" % (id,))
		
	# Create a beer
	def create_beer(self, **kwargs):
		return self.r.post("beers.json", kwargs)
		
	# Delete a beer
	def delete_beer(self, id):
		return self.r.delete("beers/%d.json" % (id,))
		
	
	# BREWERIES
		
	# Get list of all breweries
	def get_breweries(self, **kwargs):
		return self.r.get("breweries.json", kwargs)
		
	# Get brewery by id
	def get_brewery(self, id):
		return self.r.get("breweries/%d.json" % (id,))
		
	# Create a brewery
	def create_brewery(self, **kwargs):
		return self.r.post("breweries.json", kwargs)
		
	# Delete a brewery
	def delete_brewery(self, id):
		return self.r.delete("breweries/%d.json" % (id,))
		
