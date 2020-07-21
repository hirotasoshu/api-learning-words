from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import CategorySerializer
from .models import Category


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

