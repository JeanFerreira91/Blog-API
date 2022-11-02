from codecs import lookup_error
from rest_framework import serializers
from django.contrib.auth.models import User
from ApiApp.models import Post, Comment, Category


# Serializing the User model:
class UserSerializer(serializers.ModelSerializer):
    # posts field to represent the related name of the Post model:
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # comments field to represent the related name of the Comment model:
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # categories field to represent the related name of the Category model:
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        # Model associated with the serializer:
        model = User
        # Fields to be serialized from the model:
        fields = [
            'id',
            'username',
            'posts',
            'comments',
            'categories'
        ]


# Serializing the Post model:
class PostSerializer(serializers.ModelSerializer):
    # Serializing the owner field, so that it is represented by the username (instead of the id):
    owner = serializers.ReadOnlyField(source='owner.username')
    # Serializing the comments field, so that it is represented by the body of the comment:
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        # Model associated with the serializer:
        model = Post
        # Fields to be serialized from the model:
        fields = [
            'id',
            'created',
            'last_modified',
            'title',
            'body',
            'post_ready',
            'owner',
            'comments',
            'categories'
        ]
    

# Serializing the Comment model:
class CommentSerializer(serializers.ModelSerializer):
    # Serializing the owner field, so that it is represented by the username (instead of the id):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        # Model associated with the serializer:
        model = Comment
        # Fields to be serialized from the model:
        fields = [
            'id',
            'created',
            'body',
            'owner',
            'post'
        ]


# Serializing the Category model:
class CategorySerializer(serializers.ModelSerializer):
    # Serializing the owner field, so that it is represented by the username (instead of the id):
    owner = serializers.ReadOnlyField(source='owner.username')
    # Serializing the posts field, so that it is represented by the title of the post:
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        # Model associated with the serializer:
        model = Category
        # Fields to be serialized from the model:
        fields = [
            'id',
            'name',
            'owner',
            'posts'
        ]