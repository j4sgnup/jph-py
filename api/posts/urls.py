from django.urls import path
from .views import (
    UserListView,
    PostListView,
    CommentListView
)


urlpatterns = [
    path('users/', UserListView.as_view()),
    path('users/<int:userId>/posts', PostListView.as_view()),
    path('post/<int:postId>/comments', CommentListView.as_view()),
]