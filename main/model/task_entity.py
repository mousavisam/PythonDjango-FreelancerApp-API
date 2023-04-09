from django.db import models

from ..model.user_entity import User
from ..model.category_entity import Category
from ..enum.task_status import TaskStatus
from main.shared.utils import SkillTreeUtils


class Task(models.Model):
    title = models.CharField(max_length=100)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', blank=True, null=True, )
    deliver_time = models.DateField(auto_now=False)
    status = models.CharField(max_length=20, choices=TaskStatus.choices)
    description = models.TextField()
    attachments = models.FileField(upload_to=SkillTreeUtils.get_task_attachments_file_path, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='assigned_task')
    tags = models.ManyToManyField(Category)


    # def __str__(self):
    #
    #     if self.assigned_to.username:
    #         return f'client: {self.client.username}__freelancer: {self.assigned_to.username}'
    #     else:
    #         return f'client: {self.client.username}'
