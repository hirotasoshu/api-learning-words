import pytest
from pytest_factoryboy import register
from .factories import CategoryFactory, LevelFactory

register(CategoryFactory, "category")
register(CategoryFactory, "other_category")
register(LevelFactory)
register(LevelFactory, "other_level")


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def categories_url():
    return '/api/categories/'


@pytest.fixture
def levels_url():
    return '/api/levels/'

