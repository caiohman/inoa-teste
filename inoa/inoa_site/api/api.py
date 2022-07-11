import requests


class Api:
    def __init__(self):
        self.request = []

    def request_b3(self):
        self.request = requests.get('api.hgbrasil.com')
        return self.request.json()
