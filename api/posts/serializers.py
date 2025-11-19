from rest_framework import serializers
from posts.models import (
    User, 
    Post, 
    Comment, 
    UserWithPostCount, 
    PostWithCommentCount
)

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class UserWithPostCountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWithPostCount
        fields = '__all__'
class PostWithCommentCountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostWithCommentCount
        fields = '__all__'