from rest_framework import generics, permissions
from ApiApp import serializers
from django.contrib.auth.models import User
from ApiApp.models import Post, Comment, Category
from ApiApp.permissions import IsOwnerOrReadOnly

# UserList view provides read-only access (via GET) to the list of users:
class UserList(generics.ListAPIView):
    # querying the User model and returning all the users:
    queryset = User.objects.all()
    # using the UserSerializer to serialize the data:
    serializer_class = serializers.UserSerializer


# UserDetail view provides read-only access (via GET) to a single user:
class UserDetail(generics.RetrieveAPIView):
    # querying the User model and returning a single user:
    queryset = User.objects.all()
    # using the UserSerializer to serialize the data:
    serializer_class = serializers.UserSerializer


# PostList view provides read-write access (via GET, POST) to the list of posts:
class PostList(generics.ListCreateAPIView):
    # querying the Post model and returning all the posts:
    queryset = Post.objects.all()
    # using the PostSerializer to serialize the data:
    serializer_class = serializers.PostSerializer
    # using the IsOwnerOrReadOnly permission class to ensure that only the owner of a post can edit it:
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Overriding the perform_create() method to set the owner field to the current user:
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# PostDetail view provides read-write access (via GET, UPDATE and DELETE) to a single post:
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # querying the Post model and returning a single post:
    queryset = Post.objects.all()
    # using the PostSerializer to serialize the data:
    serializer_class = serializers.PostSerializer
    # using the IsOwnerOrReadOnly permission class to ensure that only the owner of a post can edit it:
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# CommentList view provides read-write access (via GET, POST) to the list of comments:
class CommentList(generics.ListCreateAPIView):
    # querying the Comment model and returning all the comments:
    queryset = Comment.objects.all()
    # using the CommentSerializer to serialize the data:
    serializer_class = serializers.CommentSerializer
    # using the IsOwnerOrReadOnly permission class to ensure that only the owner of a comment can edit it:
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Overriding the perform_create() method to set the owner field to the current user:
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# CommentDetail view provides read-write access (via GET, UPDATE and DELETE) to a single comment:
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    # querying the Comment model and returning a single comment:
    queryset = Comment.objects.all()
    # using the CommentSerializer to serialize the data:
    serializer_class = serializers.CommentSerializer
    # using the IsOwnerOrReadOnly permission class to ensure that only the owner of a comment can edit it:
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# CategoryList view provides read-write access (via GET, POST) to the list of categories:
class CategoryList(generics.ListCreateAPIView):
    # querying the Category model and returning all the categories:
    queryset = Category.objects.all()
    # using the CategorySerializer to serialize the data:
    serializer_class = serializers.CategorySerializer
    # using the IsOwnerOrReadOnly permission class to ensure that only the owner of a category can edit it:
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Overriding the perform_create() method to set the owner field to the current user:
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# CategoryDetail view provides read-write access (via GET, UPDATE and DELETE) to a single category:
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    # querying the Category model and returning a single category:
    queryset = Category.objects.all()
    # using the CategorySerializer to serialize the data:
    serializer_class = serializers.CategorySerializer
    # using the IsOwnerOrReadOnly permission class to ensure that only the owner of a category can edit it:
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
