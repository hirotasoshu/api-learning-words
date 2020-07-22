from rest_framework import serializers
from .models import *


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        icon = serializers.CharField(source='icon.url')
        fields = ('id', 'name', 'icon')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'name', 'code')


class WordSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Word
        sound = serializers.CharField(source='sound.url')
        fields = ('id', 'name', 'translation', 'transcription', 'example', 'sound')


class ThemeSerializer(DynamicFieldsModelSerializer):
    words = WordSerializer(fields=('id', 'name'), many=True, read_only=True)

    class Meta:
        model = Theme
        category = serializers.IntegerField(source='category.id')
        level = serializers.IntegerField(source='level.id')
        photo = serializers.CharField(source='photo.url')
        fields = ('id', 'category', 'level', 'name', 'photo', 'words')
