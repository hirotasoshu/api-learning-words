from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet


class ListViewSet(ListModelMixin, GenericViewSet):
    pass


class RetrieveViewSet(RetrieveModelMixin, GenericViewSet):
    pass

