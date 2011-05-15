"""
	A map of every OBDB API endpoint to a function definition in Pynt.

	Parameters that need to be embedded in the URL are treated with mustaches, e.g: {{id}}
"""

# Base OBDB API url
base_url = 'http://api.openbeerdatabase.com/v{{version}}'

api_table  = {
    # Beer methods
	'getBeers': {
		'url': '/beers.json',
		'method': 'GET',
	},
	'getBeer': {
		'url': '/beers/{{id}}.json',
		'method': 'GET',
	},
	
	# Brewery methods
	'getBreweries': {
		'url': '/breweries.json',
		'method': 'GET',
	},
	'getBrewery': {
		'url': '/breweries/{{id}}.json',
		'method': 'GET',
	},
}
