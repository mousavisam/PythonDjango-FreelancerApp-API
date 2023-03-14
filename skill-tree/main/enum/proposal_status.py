from django.db import models


class ProposalStatus(models.TextChoices):
    FAILED = "FAILED"
    SUCCESSFUL = "SUCCESSFUL"
