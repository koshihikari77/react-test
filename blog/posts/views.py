
from rest_framework import generics,permissions

from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer, UserSerializer

# ListCreateAPIView -> read-write endpoint
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# RetrieveUpdateDestoryAPIView -> ALlows read, update, delete
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# 追加
class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# 追加
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer