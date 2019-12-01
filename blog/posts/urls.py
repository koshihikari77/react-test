# posts/urls.py
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostList, PostDetail, UserList, UserDetail


router = SimpleRouter()
router.register('users', UserViewset, base_name='users')
router.register('', PostViewSet, base_name='posts')

urlpatterns = router.urls