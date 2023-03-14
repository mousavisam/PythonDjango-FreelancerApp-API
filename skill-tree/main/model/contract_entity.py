from django.db import models
from ..model.proposal_entity import Proposal
from ..enum.payment_type import PaymentType


class Contract(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.DO_NOTHING)
    rate = models.PositiveIntegerField(max_length=2)
    status = models.CharField(max_length=20, choices=ContractStatus)
    delivery_time_in_day = models.PositiveIntegerField()
    payment_amount = models.DecimalField(max_digits=12, decimal_places=3)
    payment_type = models.CharField(max_length=20, choices=PaymentType.choices)
    creation_time = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField(auto_now=False)
    end_time = models.DateTimeField(auto_now=False)
