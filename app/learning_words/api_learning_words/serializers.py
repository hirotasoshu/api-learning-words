from rest_framework import serializers
from .utils.serializers import DynamicFieldsModelSerializer
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        icon = serializers.URLField(source='icon.url')
        fields = ('id', 'name', 'icon')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'name', 'code')


class WordSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Word
        sound = serializers.URLField(source='sound.url')
        fields = ('id', 'name', 'translation', 'transcription', 'example', 'sound')


class ThemeSerializer(DynamicFieldsModelSerializer):
    words = WordSerializer(fields=('id', 'name'), many=True, read_only=True)

    class Meta:
        model = Theme
        category = serializers.IntegerField(source='category.id')
        level = serializers.IntegerField(source='level.id')
        photo = serializers.URLField(source='photo.url')
        fields = ('id', 'category', 'level', 'name', 'photo', 'words')
