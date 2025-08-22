import requests
import allure

from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    object_id = None

    @allure.step('Creating an object')
    def create_object(self, body=None):
        body = body if body else self.body
        self.response = requests.post(self.url, json=body)
        self.json = self.response.json()
        self.object_id = self.json['id']
        return self.response
