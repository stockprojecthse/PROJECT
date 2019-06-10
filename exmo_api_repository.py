import urllib
import http.client
import json

class ExmoApiRepository:
    
    API_URL = "api.exmo.com"
    HEADERS = {"Content-type": "application/x-www-form-urlencoded" }
    STATUS_OK = 200

    def callMethod(self, method, params = { }):
        connection = http.client.HTTPSConnection(self.API_URL)
        payload = urllib.parse.urlencode(params)
        connection.request("POST", "/v1/" + method, payload, self.HEADERS)
        response = connection.getresponse()
        if response.status != self.STATUS_OK:
            raise RuntimeError(response.reason)
        data = json.load(response)
        connection.close()
        return data
