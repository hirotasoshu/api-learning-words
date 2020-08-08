import pytest
from pytest_factoryboy import register, LazyFixture
from .factories import CategoryFactory, LevelFactory, ThemeFactory, WordFactory

register(CategoryFactory)
register(CategoryFactory, "other_category")
register(LevelFactory)
register(LevelFactory, "other_level")
register(ThemeFactory, category=LazyFixture("category"), level=LazyFixture("level"))
register(ThemeFactory, "theme_other_category", category=LazyFixture("other_category"), level=LazyFixture("level"))
register(ThemeFactory, "theme_other_level", category=LazyFixture("category"), level=LazyFixture("other_level"))
register(ThemeFactory, "theme_other_category_level",
         category=LazyFixture("other_category"), level=LazyFixture("other_level"))
register(WordFactory, theme=LazyFixture("theme"))


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


@pytest.fixture
def themes_url():
    return '/api/themes/'


@pytest.fixture
def word_url():
    return '/api/words/1/'


@pytest.fixture
def categories(category, other_category):
    return [category, other_category]


@pytest.fixture
def levels(level, other_level):
    return [level, other_level]


@pytest.fixture
def themes(theme, theme_other_category, theme_other_level, theme_other_category_level):
    return [theme, theme_other_category, theme_other_level, theme_other_category_level]
