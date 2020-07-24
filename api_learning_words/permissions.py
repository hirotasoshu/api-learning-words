from django.conf import settings
from rest_framework.permissions import BasePermission


class CheckApiKeyAuth(BasePermission):
    def has_permission(self, request, view):
        # Secret should be in request headers to authenticate requests
        api_secret = request.META['HTTP_SECRET']
        return api_secret == settings.API_SECRET

