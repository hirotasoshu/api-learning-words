import pytest


class TestPermission:
    @pytest.mark.parametrize('url', [
        pytest.lazy_fixture('categories_url'),
        pytest.lazy_fixture('levels_url'),
        pytest.lazy_fixture('themes_url'),
        pytest.lazy_fixture('word_url')
    ])
    @pytest.mark.django_db
    def test_without_api_secret(self, api_client, url):
        response = api_client.get(url)
        assert response.status_code == 403

    @pytest.mark.django_db
    @pytest.mark.parametrize('url', [
        pytest.lazy_fixture('categories_url'),
        pytest.lazy_fixture('levels_url'),
        pytest.lazy_fixture('themes_url'),
        pytest.lazy_fixture('word_url')
    ])
    @pytest.mark.parametrize('secret, status_code', [
        ('123', 403),
        ('TEST', 403),
        ('test', 403),
        ('T3ST', 403),
        ('t3st', 200)
    ], ids=[
        'wrong_secret',
        '1st_similar_secret',
        '2nd_similar_secret',
        '3d_similar_secret',
        'right_secret'
    ])
    def test_with_api_secret(self, api_client, url, secret, status_code, word):
        # pass word fixture to the function so that the database contains at least one word, otherwise we will get
        # 404 status code with right api_secret
        response = api_client.get(url, HTTP_SECRET=secret)
        assert response.status_code == status_code

    @pytest.mark.django_db
    @pytest.mark.parametrize('url', [
        '/api/randoms',
        '/api/categories/1/',
        '/api/levels/1/',
        '/api/words/'
    ], ids=[
        'random',
        'category_retrieve',
        'level_retrieve',
        'word_list'
    ])
    def test_invalid_urls(self, api_client, url, category, level, word):
        # pass fixtures to the function so that database contains at least one instance,
        # so we are pretty sure this is a 404 status code due to a wrong url
        response = api_client.get(url, HTTP_SECRET='t3st')
        assert response.status_code == 404


class TestCategoryViewSet:
    @pytest.mark.django_db
    def test_without_content(self, api_client, categories_url):
        response = api_client.get(categories_url, HTTP_SECRET='t3st')
        data = response.json()
        assert len(data) == 0

    @pytest.mark.django_db
    def test_with_content(self, api_client, categories_url, categories):
        response = api_client.get(categories_url, HTTP_SECRET='t3st')
        data = response.json()
        assert len(data) == 2
        for i in range(2):
            assert data[i] == {'id': categories[i].id, 'name': categories[i].name,
                               'icon': 'http://testserver' + categories[i].icon.url}


class TestLevelViewSet:
    @pytest.mark.django_db
    def test_without_content(self, api_client, levels_url):
        response = api_client.get(levels_url, HTTP_SECRET='t3st')
        data = response.json()
        assert len(data) == 0

    @pytest.mark.django_db
    def test_with_content(self, api_client, levels_url, levels):
        response = api_client.get(levels_url, HTTP_SECRET='t3st')
        data = response.json()
        assert len(data) == 2
        for i in range(2):
            assert data[i] == {'id': levels[i].id, 'name': levels[i].name, 'code': levels[i].code}


class TestWordViewSet:
    @pytest.mark.django_db
    def test_without_content(self, api_client, word_url):
        response = api_client.get(word_url, HTTP_SECRET='t3st')
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_with_content(self, api_client, word_url, word):
        response = api_client.get(word_url, HTTP_SECRET='t3st')
        data = response.json()
        assert data == {'id': word.id, 'name': word.name, 'translation': word.translation,
                        'transcription': word.transcription, 'example': word.example,
                        'sound': 'http://testserver' + word.sound.url}


class TestThemeViewSet:
    @pytest.mark.django_db
    def test_retrieve(self, api_client, themes_url, theme, word):
        response = api_client.get(themes_url + '1/', HTTP_SECRET='t3st')
        data = response.json()
        assert data == {'id': theme.id, 'category': theme.category.id, 'level': theme.level.id, 'name': theme.name,
                        'photo': 'http://testserver' + theme.photo.url, 'words': [{'id': word.id, 'name': word.name}]}

    @pytest.mark.django_db
    def test_list_without_content(self, api_client, themes_url):
        response = api_client.get(themes_url, HTTP_SECRET='t3st')
        data = response.json()
        assert len(data) == 0

    @pytest.mark.django_db
    def test_list_without_query(self, api_client, themes_url, themes):
        response = api_client.get(themes_url, HTTP_SECRET='t3st')
        data = response.json()
        assert len(data) == 4
        for i in range(4):
            assert data[i] == {'id': themes[i].id, 'category': themes[i].category.id, 'level': themes[i].level.id,
                               'name': themes[i].name, 'photo': 'http://testserver' + themes[i].photo.url}

    @pytest.mark.django_db
    @pytest.mark.parametrize('test_category', [
        pytest.lazy_fixture('category'),
        pytest.lazy_fixture('other_category')
    ])
    def test_list_query_category(self, api_client, themes_url, themes, test_category):
        response = api_client.get(themes_url, HTTP_SECRET='t3st', data={'category': test_category.id})
        data = response.json()
        assert len(data) == 2
        for i in range(2):
            assert data[i]['category'] == test_category.id

    @pytest.mark.django_db
    @pytest.mark.parametrize('test_level', [
        pytest.lazy_fixture('level'),
        pytest.lazy_fixture('other_level')
    ])
    def test_list_query_level(self, api_client, themes_url, themes, test_level):
        response = api_client.get(themes_url, HTTP_SECRET='t3st', data={'level': test_level.id})
        data = response.json()
        assert len(data) == 2
        for i in range(2):
            assert data[i]['level'] == test_level.id

    @pytest.mark.django_db
    @pytest.mark.parametrize('test_category', [
        pytest.lazy_fixture('category'),
        pytest.lazy_fixture('other_category')
    ])
    @pytest.mark.parametrize('test_level', [
        pytest.lazy_fixture('level'),
        pytest.lazy_fixture('other_level')
    ])
    def test_list_query_category_level(self, api_client, themes_url, themes, test_category, test_level):
        response = api_client.get(themes_url, HTTP_SECRET='t3st', data={'category': test_category.id,
                                                                        'level': test_level.id})
        data = response.json()
        assert len(data) == 1
        assert data[0]['category'] == test_category.id
        assert data[0]['level'] == test_level.id
