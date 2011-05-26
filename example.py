#!/usr/bin/python

from pynt import Pynt

# Instantiate Pynt object
p = Pynt()

'''
# Get the beer with id = 2
print p.get_beer(4)
'''

'''
# Create a new beer
beer_data = {
    "name"        : "Strawberry Harvest",
    "description" : "Strawberry Harvest Lager is a wheat beer ...",
    "abv"         : 4.2
  }
print p.create_beer(brewery_id=1, beer=beer_data)
'''

'''
# Delete a beer
print p.delete_beer(5)
'''

# Get all beers
print p.get_beers()

'''
# Get second page of beers, five at a time
print p.get_beers(page=2, per_page=5)
'''
