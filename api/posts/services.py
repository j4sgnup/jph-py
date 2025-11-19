import requests
from posts.models import (
    User, 
    Post, 
    Comment, 
    UserWithPostCount, 
    PostWithCommentCount
)
import logging
from django.conf import settings

logger  = logging.getLogger(__name__)
apiUrl = settings.JPH_BASE_URL

class UsersService:
    # get all users, private
    def __getAllUsers(self) -> list[User]:
        try:
            response = requests.get(f"{apiUrl}/users")
            data = response.json()
            users = [User(**item) for item in data]
            
            # users:list[User] = [] # empty users array

            # for item in data:
            #     # create a temp user object
            #     user = User(
            #         id = item.get("id"),
            #         name = item.get("name"),
            #         username = item.get("username"),
            #         email = item.get("email") 
            #     )
            #     # add temp object to users array
            #     users.append(user)

            return users
        
        except requests.RequestException as e:
            logger.error(f"Error fetching users in service:{e}")
            return []
    
    # get an user by id
    def getUserById(self, userId) -> User:
        try:
            response = requests.get(f"{apiUrl}/users/{userId}")
            data = response.json()
            user = User(**data)

            # user = User(
            #     id = data.get("id"),
            #     name = data.get("name"),
            #     username = data.get("username"),
            #     email = data.get("email") 
            # )
            return user
        
        except requests.RequestException as e:
            logger.error(f"Error fetching users by id in service:{e}")
            return []
    
    # get all post by an user, private
    def __getAllPostsByUserId(self, userId) -> list[Post]:
        try:
            response = requests.get(f"{apiUrl}/posts?userId={userId}")
            data = response.json()
            posts = [Post(**item) for item in data]
            
            # posts:list[Post] = []

            # for item in data:
            #     post = Post(
            #         userId = item.get("userId"),
            #         id = item.get("id"),
            #         title = item.get("title"),
            #         body = item.get("body"),
            #     )
            #     posts.append(post)

            return posts
        
        except requests.RequestException as e:
            logger.error(f"Error fetching posts by user id in service:{e}")
            return []
    
    # get all post by an user with copmment count
    def getPostsWithCommentCountByUserId(self, userId) -> list[PostWithCommentCount]:
        posts = self.__getAllPostsByUserId(userId)
        postsWithCommentCount: list[PostWithCommentCount] = []

        if posts:
            for post in posts:
                postId = post.id
                comments = self.getCommentsByPostId(postId)
                commentCount = len(comments) if comments else 0
                postsWithCommentCount.append(
                    self.__convertPostToPostWithCommentCount(post, commentCount)
                )
        return postsWithCommentCount
    
    # get all users with post count
    def getUsersWithPostCount(self) -> list[UserWithPostCount]:
        users = self.__getAllUsers()
        usersWithPostCount: list[UserWithPostCount] = []
        if users:
            for user in users:
                userId = user.id
                posts = self.__getAllPostsByUserId(userId)
                postCount = len(posts) if posts else 0
                usersWithPostCount.append(
                    self.__convertUserToUserWithPostCount(user, postCount)
                )
        return usersWithPostCount
    
    # get comments for a post
    def getCommentsByPostId(self, postId) -> list[Comment]:
        try:
            response = requests.get(f"{apiUrl}/comments?postId={postId}")
            data = response.json()
            comments = [Comment(**item) for item in data]
            
            # comments:list[Comment] = []

            # for item in data:
            #     comment = Comment(
            #         postId = item.get("postId"),
            #         id = item.get("id"),                    
            #         name = item.get("a"),
            #         email = item.get("email"),
            #         body = item.get("body")
            #     )
            #     comments.append(comment)
            
            return comments
        
        except requests.RequestException as e:
            logger.error(f"Error fetching comments by post id in service:{e}")
            return []
    
    # convert a Post object to PostWithCommentCount object, private
    def __convertPostToPostWithCommentCount(self, post:Post, commentCount:int) -> PostWithCommentCount:
        pwcc = PostWithCommentCount(
            post = post,
            commentCount = commentCount
        )
        return pwcc
    
    # convert a User object to UserWithPostCount object, private
    def __convertUserToUserWithPostCount(self, user:User, postCount:int) -> UserWithPostCount:
        uwpc = UserWithPostCount(
            user = user,
            postCount = postCount
        )
        return uwpc
