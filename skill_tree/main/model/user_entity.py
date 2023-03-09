from django.contrib.auth.models import AbstractUser
from django.db import models

from ..enum.user_type import UserType


class User(AbstractUser):
    type = models.CharField(max_length=30, choices=UserType.choices)
    creation_time = models.DateTimeField(auto_now_add=True)
