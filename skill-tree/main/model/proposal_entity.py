from django.db import models
from ..model.user_entity import User
from ..model.task_entity import Task
from ..enum.proposal_status import ProposalStatus


class Proposal(models.Model):
    Freelancer = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    delivery_time_in_day = models.PositiveIntegerField()
    payment_amount = models.DecimalField(max_digits=12, decimal_places=3)
    creation_time = models.DateTimeField(auto_now=False)
    status = models.CharField(max_length=20, choices=ProposalStatus.choices)
    description = models.TextField()
