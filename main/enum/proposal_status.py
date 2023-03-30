from django.db import models


class ProposalStatus(models.TextChoices):
    REJECT = "REJECT"
    ACCEPT = "ACCEPT"
