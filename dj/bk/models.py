from django.db import models


def image_path(obj, filename):
    # file will be uploaded to 
    # MEDIA_ROOT/imgs/<item-name>/<filename>
    return 'imgs/{0}/{1}'.format(obj.name, filename)


# Create your models here.

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
    image = models.FileField(upload_to=image_path)
    difficult = models.CharField(max_length=10, choices=DIFFICULTS,
                                 default="EASY")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
