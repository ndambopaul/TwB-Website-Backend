from django.urls import path
from apps.blog.views import PostAPIView, PostDetailAPIView, PostCommentAPIView

urlpatterns = [
    path("posts/", PostAPIView.as_view(), name="posts"),
    path("posts/<int:pk>/", PostDetailAPIView.as_view(), name="post-details"),
    path("posts-comments/", PostCommentAPIView.as_view(), name="post-comments"),
]
