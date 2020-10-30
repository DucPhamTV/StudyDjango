from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View, DetailView

from rest_framework import viewsets, permissions
from .serializer import (
    UserSerializer,
    ItemSerializer,
    CommentSerializer,
    ImageSerializer,
)

# Create your views here.
from .models import Item, Comment, Image
from django.contrib.auth.models import User

from .permissions import IsOwnerOrReadOnly


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    List all items, or create a new item.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Create your views here.
class IndexView(ListView):
    template_name = 'bk/index.html'
    context_object_name = "items"

    def get_queryset(self):
        result = []
        for item in Item.objects.all():
            result.append({'it': item, 'im': item.images.all()[0].image.url})

        return result


class ItemDetailView(DetailView):
    template_name = 'bk/item_detail.html'
    context_object_name = 'item'
    model = Item

    def get_object(self):
        item = get_object_or_404(Item, pk=self.kwargs['pk'])
        images = item.images.all()
        return {
            'it': item,
            'im': images,
        }
