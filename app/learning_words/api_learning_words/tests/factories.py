import factory
from learning_words.api_learning_words.models import Category, Level, Theme, Word


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f'test_category_name_{n}')
    icon = factory.django.ImageField(filename=factory.Sequence(lambda n: f'category_{n}.png'))


class LevelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Level

    name = factory.Sequence(lambda n: f'Level: {n}')
    code = factory.Sequence(lambda n: f'A{n}')


class ThemeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Theme

    category = factory.SubFactory(CategoryFactory)
    level = factory.SubFactory(LevelFactory)
    name = factory.Sequence(lambda n: f'Test theme {n}')
    photo = factory.django.ImageField(filename=factory.Sequence(lambda n: f'theme_{n}.png'))


class WordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Word





