from django.db import models

from common.models import AbstractTimedModel


class User(AbstractTimedModel):
    account = models.CharField(max_length=200, unique=True, null=False)
    password = models.CharField(max_length=200, null=False)
    username = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=255, null=False)
