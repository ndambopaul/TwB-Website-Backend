from django.shortcuts import render

from rest_framework import generics

from apps.blog.models import Post, PostComment
from apps.blog.serializers import PostSerializer, PostCommentSerializer


# Create your views here.
class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    lookup_field = "pk"


class PostCommentAPIView(generics.ListCreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer

    def get_queryset(self):
        post = self.request.query_params.get("post")
        if post:
            return self.queryset.filter(post_id=post)
        return []
