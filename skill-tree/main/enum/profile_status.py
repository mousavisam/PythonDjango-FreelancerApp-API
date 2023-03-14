from django.db import models


class ProfileStatus(models.TextChoices):
    BUSY = "BUSY"
    FREE = "FREE"
