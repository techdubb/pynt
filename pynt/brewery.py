from request import Request

class Brewery(object):
        
    @classmethod
    def all(self, **kwargs):
        return Request.get("breweries.json", kwargs)
        
    @classmethod
    def get(self, id):
        return Request.get("breweries/%d.json" % (id,))
        
    @classmethod
    def create(self, **kwargs):
        return Request.post("breweries.json", kwargs)
        
    @classmethod
    def delete(self, id):
        return Request.delete("breweries/%d.json" % (id,))
        
