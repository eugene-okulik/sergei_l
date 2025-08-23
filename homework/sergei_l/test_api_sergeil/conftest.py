import pytest

from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.put_object import PutObject
from endpoints.patch_object import PatchObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def put_object_endpoint():
    return PutObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def create_delete_test_object(create_object_endpoint, delete_object_endpoint):
    create_object_endpoint.create_object()
    create_object_endpoint.assert_response_status_is_200()
    yield create_object_endpoint.object_id
    delete_object_endpoint.delete_object(create_object_endpoint.object_id)
    delete_object_endpoint.assert_response_status_is_200()


@pytest.fixture()
def create_test_object(create_object_endpoint):
    create_object_endpoint.create_object()
    create_object_endpoint.assert_response_status_is_200()
    return create_object_endpoint.object_id
