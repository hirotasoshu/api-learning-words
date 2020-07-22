from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'levels', views.LevelViewSet)
router.register(r'words', views.WordViewSet)
router.register(r'themes', views.ThemeViewSet, basename='Theme')
urlpatterns = router.urls
