import pytest
from pytest_factoryboy import register
from .factories import CategoryFactory

register(CategoryFactory)
register(CategoryFactory, "other_category")


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def categories_url():
    return '/api/categories/'

