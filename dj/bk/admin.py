from django.contrib import admin

# Register your models here.
from .models import Item, Category, Image, Comment


admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Comment)

