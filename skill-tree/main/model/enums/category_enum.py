from django.db import models


class Category(models.TextChoices):
    SOFTWARE = "SOFTWARE"
    MARKETING = "MARKETING"
    DESIGN = "DESIGN"
