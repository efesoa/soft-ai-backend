import pytest
from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()


@pytest.mark.django_db
def test_get_clients():
    pass
