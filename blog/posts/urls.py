# posts/urls.py
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewset, PostViewSet

router = SimpleRouter()
router.register('users', UserViewset, base_name='users')
router.register('', PostViewSet, base_name='posts')

urlpatterns = router.urls