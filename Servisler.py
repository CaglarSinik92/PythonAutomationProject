import json

import requests
from json.decoder import JSONDecodeError


class GetOfferService:
    def __init__(self, base_url, username, password, data):
        self.response = None
        self.base_url = base_url
        self.username = username
        self.password = password
        self.data = data

    def getOfferPost(self):
        response = requests.post(self.base_url, json=self.data, auth=(self.username, self.password))
        try:
            if response.status_code == 200:
                pass
        except JSONDecodeError:
            pass
        self.response = response


class CaptureResponse:
    def __init__(self, base_url, username, password, data):
        self.response = None
        self.base_url = base_url
        self.username = username
        self.password = password
        self.data = data

    def captureResponse(self):
        response = requests.put(self.base_url, json=self.data, auth=(self.username, self.password))
        try:
            if response.status_code == 200:
                pass
        except JSONDecodeError:
            pass
        self.response = response
