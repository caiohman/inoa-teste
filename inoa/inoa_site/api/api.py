import requests
import json


class Api:
    def __init__(self):
        self.advice_message = ''
        self.response_json = []

        self.request_b3()
        self.extract_message()

    def request_b3(self):
        response = requests.get('https://api.adviceslip.com/advice')
        if response.status_code == 200:
            self.response_json = response.json()
        else:
            raise Exception('api unavailable')

    def extract_message(self):
        self.advice_message = self.response_json['slip']['advice']
