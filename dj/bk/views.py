from django.shortcuts import render
from django.views.generic import ListView, View

from rest_framework import viewsets, generics
from .serializer import UserSerializer, ItemSerializer, CommentSerializer

# Create your views here.
from .models import Item, Comment
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    List all items, or create a new item.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Create your views here.
class IndexView(ListView):
    template_name = 'bk/index.html'
    context_object_name = "items"

    def get_queryset(self):
        return Item.objects.all()



#class ItemView(View):
#    def get(self, request, name):
#        # return all question in database
#        item = Item.objects.get(name=name)
#        return render(request, 'bk/item.html', {
#            'image_url': item.image,
#            'description': item.paragraph,
#            'name': item.name,
#            #'date': item.date,
#        })
