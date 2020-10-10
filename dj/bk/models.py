from django.db import models


def image_path(obj, filename):
    # file will be uploaded to 
    # MEDIA_ROOT/imgs/<item-name>/<filename>
    return 'imgs/{0}/{1}'.format(obj.name, filename)


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    paragraph = models.CharField(max_length=5000)
    image = models.FileField(upload_to=image_path)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
