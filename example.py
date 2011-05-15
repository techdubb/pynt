from pynt import Pynt

# Instantiate Pynt without a key
obdb = Pynt()

# Get the beer with id = 2
beer = obdb.getBeer(id=2)
print beer

print "\n"

# Get all beers
beers = obdb.getBeers()
print beers
