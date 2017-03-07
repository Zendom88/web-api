from django.db.models import Q

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView
    )

from posts.models import Post
from .serializers import (
    PostCreateSerializer,
    PostListSerializer,
    PostDetailSerializer
    )


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostListAPIView (ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
    	if query:
    		queryset_list = queryset_list.filter(
    				Q(title__icontains=query)|
    				Q(content__icontains=query)|
    				Q(user__first_name__icontains=query) |
    				Q(user__last_name__icontains=query)
    				).distinct()
        return queryset_list
