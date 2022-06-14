import requests

class APIRequestor:

    def __init__(self, **kwargs):

        self.method = kwargs.get("method")
        self.url = kwargs.get("url")
        self.headers = kwargs.get("headers")
        self.data = kwargs.get("data")
    
    def get(self):
        response = requests.get(
                self.url,
                headers=self.headers,
            )
        return response
