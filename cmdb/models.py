from django.db import models

from django.db import models

from common.models import AbstractTimedModel

class AbstractUsedModel(AbstractTimedModel):
    class Meta:
        abstract = True

    # create_user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    # last_update_user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)


class MrRoomTb(AbstractUsedModel):
    room_name = models.CharField(max_length=200)

