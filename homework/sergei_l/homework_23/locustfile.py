from locust import task, HttpUser
import random


class ObjectUser(HttpUser):

    @task(1)
    def get_all_objects(self):
        self.client.get('/object')

    @task(2)
    def get_one_object(self):
        self.client.get(f'object/{random.choice([1, 1066, 1067, 1068, 1069])}')