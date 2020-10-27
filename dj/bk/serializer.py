from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Item, Comment, Image


class UserSerializer(serializers.ModelSerializer):
    # link user and its items, explicit queryset so that User can modified its items.
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())
    class Meta:
        model = User
        # Don't reveal password here
        fields = ('id', 'username', 'items')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('date', 'content', 'item')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('item', 'image', 'name')


class ItemSerializer(serializers.ModelSerializer):
    # images and comments are reverse relationship
    images = ImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=False)
    # owner is already a field in Item model
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Item
        fields = ('name', 'pub_date', 'title', 'paragraph', 'category',
                  'difficult', 'price', 'comments', 'images', 'owner')

