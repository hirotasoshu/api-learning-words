from rest_framework.viewsets import ReadOnlyModelViewSet
from django_auto_prefetching import AutoPrefetchViewSetMixin
from .serializers import CategorySerializer
from .models import Category


class CategoryViewSet(AutoPrefetchViewSetMixin, ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

