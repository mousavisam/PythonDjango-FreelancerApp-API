from django.db import models


class ContractStatus(models.TextChoices):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECT = "REJECT"


