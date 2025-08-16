import requests
import pytest


@pytest.fixture()
def create_delete_test_object():
    body = {
        "name": "test_name",
        "data": {
            "one": 1,
            "two": 2
        }
    }
    request = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    obj_id = request.json()['id']
    yield obj_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')


@pytest.fixture()
def create_test_object():
    body = {
        "name": "test_name",
        "data": {
            "one": 1,
            "two": 2
        }
    }
    request = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    obj_id = request.json()['id']
    return obj_id


@pytest.fixture(scope="session")
def session_text():
    print('Start testing')
    yield
    print('Testing complete')


@pytest.fixture()
def each_test_text():
    print('before test')
    yield
    print('after test')


@pytest.mark.parametrize('object_name', ['first_test_name', 'second_test_name', 'third_test_name'])
def test_create_object(object_name, session_text, each_test_text):
    body = {
        "name": object_name,
        "data": {
            "one": 1,
            "two": 2
        }
    }
    request = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    assert request.status_code == 200, "Wrong status code"


@pytest.mark.critical
def test_put_object(create_delete_test_object, each_test_text):
    body = {
        "name": "test_name-UPD",
        "data": {
            "two": 2
        }
    }
    request = requests.put(f'http://objapi.course.qa-practice.com/object/{create_delete_test_object}', json=body)
    assert request.status_code == 200, "Wrong status code"


@pytest.mark.medium
def test_patch_object(create_delete_test_object, each_test_text):
    body = {
        "name": "test_name-UPD-by-PATCH",
    }
    request = requests.patch(f'http://objapi.course.qa-practice.com/object/{create_delete_test_object}', json=body)
    assert request.status_code == 200, "Wrong status code"


def test_delete_object(create_test_object, each_test_text):
    request = requests.delete(f'http://objapi.course.qa-practice.com/object/{create_test_object}')
    assert request.status_code == 200, "Wrong status code"
