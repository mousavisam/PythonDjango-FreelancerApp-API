from django.db import models


class TaskStatus(models.TextChoices):
    ASSIGNED = "ASSIGNED"
    UNASSIGNED = "UNASSIGNED"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
