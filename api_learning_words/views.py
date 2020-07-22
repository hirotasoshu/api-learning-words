from rest_framework.viewsets import ReadOnlyModelViewSet
from django_auto_prefetching import AutoPrefetchViewSetMixin
from .serializers import *
from .models import *


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LevelViewSet(ReadOnlyModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

