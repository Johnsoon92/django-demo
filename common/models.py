from django.db import models
from django.contrib.auth.models import User


class AbstractTimedModel(models.Model):
    class Meta:
        abstract = True

    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(User, related_name='+', on_delete=models.DO_NOTHING)
    last_update_user = models.ForeignKey(
        User, related_name='+', on_delete=models.DO_NOTHING)
