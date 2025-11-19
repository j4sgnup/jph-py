class User:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email
        }
    
class Post:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.userId = kwargs.get("userId")
        self.title = kwargs.get("title")
        self.body = kwargs.get("body")

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.userId,
            "title": self.title,
            "body": self.body
        }
    
class Comment:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.postId = kwargs.get("postId")
        self.name = kwargs.get("name")
        self.email = kwargs.get("email")
        self.body = kwargs.get("body")

    def to_dict(self):
        return {
            "id": self.id,
            "postId": self.postId,
            "name": self.name,
            "email": self.email,
            "body": self.body
        }
    
class UserWithPostCount:
    def __init__(self, user, postCount):
        self.user =  user   
        self.postCount = postCount

    def to_dict(self):
        return {
            "user": self.user.to_dict(),
            "postCount": self.postCount
        }

class PostWithCommentCount:
    def __init__(self, post, commentCount):
        self.post =  post   
        self.commentCount = commentCount

    def to_dict(self):
        return {
            "post": self.post.to_dict(),
            "commentCount": self.commentCount
        }



'''
from django.db import models

class User(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=254)

class Post(models.Model):
    userId = models.IntegerField()
    id = models.IntegerField()
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)

class Comment(models.Model):
    postId = models.IntegerField()
    id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=254)
    body = models.TextField()

class UserWithPostCount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='with_post_count')
    postCount = models.IntegerField()

class PostWithCommentCount(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='with_comment_count')
    commentCount = models.IntegerField()


'''
