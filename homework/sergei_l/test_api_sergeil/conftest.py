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
