import requests
import allure

from endpoints.endpoint import Endpoint


class PutObject(Endpoint):

    @allure.step('Put updating of an object')
    def put_object(self, object_id, body=None):
        body = body if body else self.body
        self.response = requests.put(f'{self.url}/{object_id}', json=body)
