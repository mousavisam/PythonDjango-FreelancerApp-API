from django.db import models
from ..model.user_entity import User
from ..model.category_entity import Category
from ..enum.task_status import TaskStatus
from ..enum.payment_type import PaymentType


class Task(models.Model):
    title = models.CharField(max_length=100)
    client = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    deliver_time = models.DateField(auto_now=False)
    service_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=20, choices=TaskStatus.choices)
    description = models.TextField()
    creation_time = models.DateTimeField(auto_now=True)
