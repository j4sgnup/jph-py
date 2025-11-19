## Steps I used to creae DRF endpoints

### Prerequisites 
1. virtual env

   `python -m venv env`

2. activate 

   Win

   `cd env/Scripts && activate && cd ../../` 

    git bash

    `source env/Scripts/activate`

3. Install django and DRF
   
   `pip install django djangorestframework`

### Project
1. Create a project

   `django-admin startproject api`

2. Create app

   `cd api`
   
   `python manage.py startapp posts`

### Coding
- Create the models
  - find models.py
  - create model class: [className] (models.Model, [anyOtherClass]):
  - for fields, use [fieldName] = models.[CharFiels | IntegerField] etc
    - like `postId = models.IntegerField`
  - [API ONLY] for apps which just calls APIs and no db connection, use plain py classes
  - [API ONLY] in the constructor, use **kwargs to get data from external API response where unknown number of extra fields are possible.
  - [API ONLY] use a custom to_dict() which will be useful later
  - [API ONLY] when you need to inherit another model, just assume that a arg will be there and just use self to assign that.
  ```python
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
   ###############
   class PostWithCommentCount:
    def __init__(self, post, commentCount):
        self.post =  post   
        self.commentCount = commentCount

    def to_dict(self):
        return {
            "post": self.post.to_dict(),
            "commentCount": self.commentCount
        }

  ```
- Create the serializers
  - create serializers.py, same path as models.py
  - import serializers from rest_framework
  - import the models
    - like `from posts.models import User`
  - create serializer class for each view
    - class [ModelName]ListSerializer(serializers.ModelSerializer):
      - like class UserListSerializer(serializers.ModelSerializer):
    - Add a Meta subclass. Add model and field properties. 
    - assign the proper mode to model prop 
    - assign '__all__' to field prop 
      - like 
        ```
        model = User
        fields = '__all__'
        ```
- create services.py, same path as models.py
  - Install requests using pip
  - Import the models
  - `import logging`
  - `from django.conf import settings`
  - get config values like api bae url `apiUrl = settings.JPH_BASE_URL`
  - create class [entity name]Service
    - like `class UserService:`
  - Use try catch block to call API. In service, do not return Response
    - like 
      ```python
      try:
         response = requests.get(f"{apiUrl}/comments?postId={postId}")
         data = response.json()
         comments = [Comment(**item) for item in data]
         ....
      except requests.RequestException as e
         [logger code]...
         return [] 
      ```
      - `comments = [Comment(**item) for item in data]` pattern depicts that data is a list of dictionaries, and when you create an new Comment object, inside an array, with a loop (for ... in), then, each item in data is passed as an argument to Comment constructor, and we are using ** to unpack items, which is consumed by the **kwargs in model
- modify views.py
  - in views.py create a class for each url endpoint and use get, post etc to handle requests
  - [API ONLY] use the service directly to access service methods
  - like 
  ```python
  class CommentListView(APIView):
    user_service = UsersService()

    def get(self, request, postId):
        comments = self.user_service.getCommentsByPostId(postId)
        comments_data = [comment.to_dict() for comment in comments]
        return Response(comments_data)
  ```
  - This pattern: `[comment.to_dict() for comment in comments]` does the same as above, loops over all comments, and calls to_dict() for each comment object, which returns a dictionary. The dict is pushed into the comments_data array.


- create urls.py 
  - there will already be urls.py in the root of you app, lets say, `/api/urls.py`
  - if you want to handle multiple entities, like posts or users, then create a separate `posts/urls.py` or `users/urls.py` for your sub path like `api/posts`, `api/users`
  - in your `api/urls.py` use include() to get all the urls for your sub path
    - like
    ```python
    urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/', include('posts.urls')),
    ]
    ```
  - in your `posts/urls.py` create all the endpoints
    like
    ```python
    urlpatterns = [
      path('users/', UserListView.as_view()),
      path('users/<int:userId>/posts', PostListView.as_view()),
      path('post/<int:postId>/comments', CommentListView.as_view()),
    ]
    ```
    - `<int:postId>` means that this param will be received by your view
      - Check above in view section for `class CommentListView(APIView)`