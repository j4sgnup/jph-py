from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
# from posts.models import User
# from .serializers import UserListSerializer

from posts.services import UsersService

class UserListView(APIView):
    user_service = UsersService()

    def get(self, request):
        users = self.user_service.getUsersWithPostCount()
        users_data = [user.to_dict() for user in users]
        return Response(users_data)

class PostListView(APIView):
    user_service = UsersService()

    def get(self, request, userId):
        posts = self.user_service.getPostsWithCommentCountByUserId(userId)
        posts_data = [post.to_dict() for post in posts]
        return Response(posts_data)
    
class CommentListView(APIView):
    user_service = UsersService()

    def get(self, request, postId):
        comments = self.user_service.getCommentsByPostId(postId)
        comments_data = [comment.to_dict() for comment in comments]
        return Response(comments_data)