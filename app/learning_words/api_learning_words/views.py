from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .utils.viewsets import ListViewSet, RetrieveViewSet
from .serializers import CategorySerializer, LevelSerializer, WordSerializer, ThemeSerializer
from .permissions import CheckApiKeyAuth
from .models import *


class CategoryViewSet(ListViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CheckApiKeyAuth]


class LevelViewSet(ListViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [CheckApiKeyAuth]


class WordViewSet(RetrieveViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [CheckApiKeyAuth]


class ThemeViewSet(ViewSet):
    permission_classes = [CheckApiKeyAuth]

    def list(self, request):
        queryset = Theme.objects.select_related('category', 'level').prefetch_related('words')
        category = self.request.query_params.get('category', None)
        level = self.request.query_params.get('level', None)
        if category:
            queryset = queryset.filter(category_id=category)
        if level:
            queryset = queryset.filter(level_id=level)
        serializer = ThemeSerializer(queryset, fields=('id', 'category', 'level', 'name', 'photo'), many=True,
                                     read_only=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Theme.objects.select_related('category', 'level').prefetch_related('words')
        theme = get_object_or_404(queryset, pk=pk)
        serializer = ThemeSerializer(theme, read_only=True, context={'request': request})
        return Response(serializer.data)





