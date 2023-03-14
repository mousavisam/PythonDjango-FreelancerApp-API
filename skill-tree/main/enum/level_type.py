from django.db import models


class LevelType(models.TextChoices):
    BASIC = "BASIC"
    INTERMEDIATE = "INTERMEDIATE"
