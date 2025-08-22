import requests
import allure

from endpoints.endpoint import Endpoint


class PatchObject(Endpoint):
    @allure.step('Updating object with patch method')
    def patch_object(self, object_id, body):
        self.response = requests.patch(f'{self.url}/{object_id}', json=body)
