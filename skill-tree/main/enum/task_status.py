from django.db import models


class TaskStatus(models.TextChoices):
    ASSIGNED = "ASSIGNED"
    UNASSIGNED = "UNASSIGNED"
