from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from ..model.user_entity import User


class Rate(models.Model):
    freelancer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="freelancer_rate")
    client = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="client_rate")
    rate = models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    creation_time = models.DateTimeField(auto_now=True)
