from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import ListModelMixin
from django_auto_prefetching import AutoPrefetchViewSetMixin
from .serializers import *
from .models import *


class CategoryViewSet(ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LevelViewSet(ListModelMixin, GenericViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

