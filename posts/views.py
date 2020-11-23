
from rest_framework import generics, permissions

from .models import Post

from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostListApiView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer




