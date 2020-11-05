import uuid

from django.db import models


class PersonalInfo(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False,
                            primary_key=True)
    name = models.CharField(max_length=200)
    facebook = models.URLField(max_length=200)
    

class Phone(models.Model):
    number = models.CharField(max_length=10, primary_key=True, editable=False)
    person = models.ForeignKey(PersonalInfo, related_name='phones',
                               on_delete=models.CASCADE)
    zalo_available = models.BooleanField(null=True)


class Email(models.Model):
    address = models.CharField(max_length=10, primary_key=True, editable=False)
    person = models.ForeignKey(PersonalInfo, related_name='emails',
                               on_delete=models.CASCADE)


