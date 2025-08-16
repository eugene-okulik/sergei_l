import requests


def delete_object(obj_id):
    request = requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')
    assert request.status_code == 200, "Wrong status code"


def create_object():
    body = {
        "name": "test_name",
        "data": {
            "one": 1,
            "two": 2
        }
    }
    request = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    assert request.status_code == 200, "Wrong status code"
    return request.json()['id']


def put_object():
    obj_id = create_object()
    body = {
        "name": "test_name-UPD",
        "data": {
            "two": 2
        }
    }
    request = requests.put(f'http://objapi.course.qa-practice.com/object/{obj_id}', json=body)
    assert request.status_code == 200, "Wrong status code"
    delete_object(request.json()['id'])


def patch_object():
    obj_id = create_object()
    body = {
        "name": "test_name-UPD-by-PATCH",
    }
    request = requests.patch(f'http://objapi.course.qa-practice.com/object/{obj_id}', json=body)
    assert request.status_code == 200, "Wrong status code"
    delete_object(request.json()['id'])


create_object()
put_object()
patch_object()
delete_object(create_object())
