from django.db import models


class PaymentType(models.TextChoices):
    PER_HOUR = "PER_HOUR"
    AFTER_DONE = "AFTER_DONE"
    AFTER_SPECIFIC_PART = "AFTER_SPECIFIC_PART"
