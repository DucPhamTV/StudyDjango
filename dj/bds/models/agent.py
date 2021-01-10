import uuid

from django.db import models
from .asset import Asset
from .personal_info import PersonalInfo


class Agent(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False,
                            primary_key=True)

    person_info = models.OneToOneField(PersonalInfo, on_delete=models.SET_NULL, null=True)
    posted_assets = models.ForeignKey(Asset, on_delete=models.SET_NULL,
                                      null=True)
