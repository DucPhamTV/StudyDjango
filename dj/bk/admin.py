from django.contrib import admin

# Register your models here.
from .models import Item, Category, Image, Comment

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Comment)

