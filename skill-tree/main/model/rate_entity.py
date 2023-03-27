from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from ..model.user_entity import User


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_rate", blank=True, null=True)
    rate = models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    creation_time = models.DateTimeField(auto_now=True)
