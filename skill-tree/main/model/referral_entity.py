from django.db import models
from ..model.user_entity import User


class Referral(models.Model):
    referee = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    referer = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now=True)
