from pynt import Pynt

# Instantiate Pynt without a key
obdb = Pynt()

# Get the beer with id = 2
beer = obdb.get_beer(2)
print beer

print "\n"

# Get all beers
beers = obdb.get_beers()
print beers

print "\n"

# Get second page of beers, five at a time
beers = obdb.get_beers(page=2, per_page=5)
print beers
