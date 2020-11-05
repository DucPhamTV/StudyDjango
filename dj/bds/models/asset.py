import uuid

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, default="")

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, default="")

    def __str__(self):
        return self.name


class Asset(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    urls = models.URLField(max_length=200)
    area = models.IntegerField(null=True)
    address = models.ForeignKey(Address, related_name='assets')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True)


class Address(models.Model):
    addr = TextField(max_length=200, default="")
    street = TextField(max_length=200, default="")
    district = models.ForeignKey(District, on_delete=models.SET_NULL,
                                 null=True)
    Province = models.ForeignKey(Province, on_delete=models.SET_NULL,
                                 null=True)



