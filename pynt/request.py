from httplib2 import Http
from urllib import quote
from simplejson import dumps, loads
from settings import Settings

class Request(object):

    # Handle GET requests
    @classmethod
    def get(self, path, parameters = {}):
        parameters['token'] = Settings.public_token

        # dict to query string from: http://bit.ly/k1fAsx
        query_string = '&'.join([k+'='+quote(str(v)) for (k,v) in parameters.items()])
        path = "%s%s?%s" % (Settings.host, path, query_string,)

        return self.request(path)

    # Handle POST requests  
    @classmethod
    def post(self, path, parameters={}):
        parameters['token'] = Settings.private_token

        path = "%s%s" % (Settings.host, path,)
        options = {
            'request_type' : 'POST',
            'body' : dumps(parameters),
            'headers' : {'Content-Type': 'application/json'}
        }

        return self.request(path, options)

    # Handle DELETE requests
    @classmethod    
    def delete(self, path):
        path = "%s%s" % (Settings.host, path,)
        options = {
            'request_type' : 'DELETE',
            'body' : dumps({'token': Settings.private_token}),
            'headers' : {'Content-Type': 'application/json'}
        }

        return self.request(path, options)

    @classmethod
    def request(self, path, options = {}):
        client = Http()

        if len(options) == 0:
            resp, content = client.request(path)
        else:
            resp, content = client.request(
                path, 
                options['request_type'], 
                body = options['body'], 
                headers = options['headers']
            )

        try:
            return loads(content)
        except:
            return content 
