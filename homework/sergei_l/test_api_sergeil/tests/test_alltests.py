import pytest


@pytest.mark.parametrize('object_name', ['first_test_name', 'second_test_name', 'third_test_name'])
def test_create_object(create_object_endpoint, object_name):
    body = {
        "name": object_name,
        "data": {
            "one": 1,
            "two": 2
        }
    }
    create_object_endpoint.create_object(body)
    create_object_endpoint.assert_response_status_is_200()


def test_put_object(create_delete_test_object, put_object_endpoint):
    body = {
        "name": "test_name-UPD",
        "data": {
            "two": 2
        }
    }
    put_object_endpoint.put_object(create_delete_test_object, body)
    put_object_endpoint.assert_response_status_is_200()


def test_patch_object(create_delete_test_object, patch_object_endpoint):
    body = {
        "name": "test_name-UPD-by-PATCH",
    }
    patch_object_endpoint.patch_object(create_delete_test_object, body)
    patch_object_endpoint.assert_response_status_is_200()


def test_delete_object(create_test_object, delete_object_endpoint):
    delete_object_endpoint.delete_object(create_test_object)
    delete_object_endpoint.assert_response_status_is_200()
