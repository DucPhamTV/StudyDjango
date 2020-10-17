from django.db import models


def image_path(obj, filename):
    # file will be uploaded to 
    # MEDIA_ROOT/imgs/<item-name>/<filename>
    return 'imgs/{0}/{1}'.format(obj.name, filename)


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.category


class Item(models.Model):
    DIFFICULTS = [
        ("EASY", "Easy"),
        ("MEDIUM", "Medium"),
        ("HARD", "Hard"),
        ("HARDEST", "Hardest"),
    ]
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    title = models.TextField(max_length=200, default="")
    paragraph = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True)
    difficult = models.CharField(max_length=10, choices=DIFFICULTS,
                                 default="EASY")
    price = models.IntegerField(null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Image(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE) 
    image = models.ImageField(upload_to=image_path)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Comment(models.Model):
    date = models.DateTimeField('date published')
    content = models.TextField()
    item = models.ForeignKey(Item, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.content
