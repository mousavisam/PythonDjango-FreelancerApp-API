from django.db import models


class UserType(models.TextChoices):
    ADMIN = "ADMIN"
    FREELANCER = "FREELANCER"
    CLIENT = "CLIENT"

