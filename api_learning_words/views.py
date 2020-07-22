from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import ListModelMixin
from django_auto_prefetching import AutoPrefetchViewSetMixin
from .serializers import *
from .models import *

class ListViewSet(ListModelMixin, GenericViewSet):
    pass

class CategoryViewSet(ListViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LevelViewSet(ListViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

