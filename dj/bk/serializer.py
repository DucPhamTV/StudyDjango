from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Item, Comment, Image


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('date', 'content', 'item')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('item', 'image', 'name')


class ItemSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=False)

    class Meta:
        model = Item
        fields = ('name', 'pub_date', 'title', 'paragraph', 'category',
                  'difficult', 'price', 'images', 'comments')

