from django.db.models import QuerySet

from ....enum.task_status import TaskStatus
from ....model.category_entity import Category
from ....model.task_entity import Task
from ....model.user_entity import User


class TaskDao:

    def insert_task(self, **kwargs) -> None:
        tags = kwargs['tags']
        kwargs.pop('tags')
        task = Task.objects.create(**kwargs)
        task.tags.set(tags)
        task.save()

    def get_task_by_id(self, task_id: int) -> Task:
        return Task.objects.filter(id=task_id).first()

    def update_task_attachments(self, task: Task, filename: str) -> None:
        task.attachments = filename
        task.save()

    def update_task_status(self, task: Task, task_status: TaskStatus) -> None:
        task.status = task_status
        task.save()

    def set_freelancer_for_task(self, user: User, task: Task) -> None:
        task.assigned_to = user
        task.save()

    def get_task_by_tag(self, tag: str) -> QuerySet:
        return Task.objects.filter(tags__title__icontains=tag)

    def get_task_by_title(self, title: str) -> QuerySet:
        return Task.objects.filter(title__icontains=title)



