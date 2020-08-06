import pytest


class TestCategoryViewSet:
    @pytest.mark.django_db
    def test_without_api_secret(self, api_client, categories_url):
        response = api_client.get(categories_url)
        assert response.status_code == 403

    @pytest.mark.django_db
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
    def test_with_api_secret(self, api_client, categories_url, secret, status_code):
        response = api_client.get(categories_url, HTTP_SECRET=secret)
        assert response.status_code == status_code

    @pytest.mark.django_db
    def test_without_content(self, api_client, categories_url):
        response = api_client.get(categories_url, HTTP_SECRET='t3st')
        data = response.json()
        assert len(data) == 0

    @pytest.mark.django_db
    def test_with_content(self, api_client, categories_url, category, other_category):
        response = api_client.get(categories_url, HTTP_SECRET='t3st')
        data = response.json()
        assert len(data) == 2
        assert data[0] == {'id': category.id, 'name': category.name, 'icon': 'http://testserver' + category.icon.url}
        assert data[1] == {'id': other_category.id, 'name': other_category.name, 'icon': 'http://testserver' +
                                                                                         other_category.icon.url}




