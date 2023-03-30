from django.contrib.auth.models import AbstractUser
from django.db import models

from ..enum.user_status import UserType


class User(AbstractUser):
    type = models.CharField(max_length=20, choices=UserType.choices, blank=True, null=True)
    register_time = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=80, unique=True, null=False)



