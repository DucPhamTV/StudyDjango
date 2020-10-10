from django.shortcuts import render
from django.views.generic import ListView, View

# Create your views here.
from .models import Item

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
