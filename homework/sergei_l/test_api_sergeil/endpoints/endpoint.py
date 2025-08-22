import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    body = {
        "name": "test_name",
        "data": {
            "one": 1,
            "two": 2
        }
    }

    @allure.step('Checking if response is correct')
    def assert_response_status(self):
        print(self.response)
        assert self.response.status_code == 200, 'Wrong status code'