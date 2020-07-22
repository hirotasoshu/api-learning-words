from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from .serializers import CategorySerializer, LevelSerializer, WordSerializer, ThemeSerializer
from .models import *
from rest_framework.response import Response


class ListViewSet(ListModelMixin, GenericViewSet):
    pass


class RetrieveViewSet(RetrieveModelMixin, GenericViewSet):
    pass


class CategoryViewSet(ListViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LevelViewSet(ListViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class WordViewSet(RetrieveViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class ThemeViewSet(ViewSet):
    def list(self, request):
        queryset = Theme.objects.select_related('category', 'level').prefetch_related('words')
        category = self.request.query_params.get('category', None)
        level = self.request.query_params.get('level', None)
        if category:
            queryset = queryset.filter(category_id=category)
        if level:
            queryset = queryset.filter(level_id=level)
        serializer = ThemeSerializer(queryset, fields=('id', 'category', 'level', 'name', 'photo'), many=True,
                                     read_only=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Theme.objects.select_related('category', 'level').prefetch_related('words')
        theme = get_object_or_404(queryset, pk=pk)
        serializer = ThemeSerializer(theme, read_only=True)
        return Response(serializer.data)





