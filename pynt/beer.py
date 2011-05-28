from request import Request

class Beer(object):

	@classmethod
	def all(self, **kwargs):
		return Request.get("beers.json", kwargs)
		
	@classmethod
	def get(self, id):
		return Request.get("beers/%d.json" % (id,))
	
	@classmethod	
	def create(self, **kwargs):
		return Request.post("beers.json", kwargs)
	
	@classmethod	
	def delete(self, id):
		return Request.delete("beers/%d.json" % (id,))
