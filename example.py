from pynt.pynt import Settings, Beer

# Setting options
Settings.host = 'http://api.localhost:3000/v1/'
Settings.public_token = 'YOUR_PUBLIC_TOKEN'
Settings.private_token = 'YOUR_PRIVATE_TOKEN'


# Get all beers
print Beer.all()

'''
# Get the beer with id 2
print Beer.get(2)
'''

'''
# Create a new beer
beer_data = {
    "name"        : "Strawberry Harvest",
    "description" : "Strawberry Harvest Lager is a wheat beer ...",
    "abv"         : 4.2
}
print Beer.create(brewery_id = 1, beer = beer_data)
'''

'''
# Delete beer with id 5
print Beer.delete(5)
'''
