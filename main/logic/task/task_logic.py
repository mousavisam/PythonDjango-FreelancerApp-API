from typing import Union, Optional

from django.core.exceptions import ObjectDoesNotExist

from main.enum.task_status import TaskStatus
from main.logic.category.category_logic import CategoryLogic
from main.logic.dao.task.task_dao import TaskDao
from main.model.task_entity import Task
from main.model.user_entity import User


class TaskLogic:

    def __init__(self):
        super().__init__()
        self.dao = TaskDao()
        self.category_logic = CategoryLogic()

    def insert_task(self, **kwargs):
        category = self.category_logic.get_category_by_title(title=kwargs['service_category'])
        if category:
            kwargs['service_category'] = category
            kwargs['status'] = TaskStatus.UNASSIGNED
            self.dao.insert_task(**kwargs)

        else:
            raise ObjectDoesNotExist

    def get_task_by_id(self, task_id: int) -> Task:
        return self.dao.get_task_by_id(task_id)

    def update_task_attachments(self, task_id: int, filename: str) -> None:
        task = self.get_task_by_id(task_id)
        self.dao.update_task_attachments(task, filename)

    def update_task_status(self, task_status: TaskStatus, task: Task) -> None:
        self.dao.update_task_status(task_status=task_status, task=task)

    def make_task_done(self, task_id: int, user) -> None:
        task = self.get_task_by_id(task_id)
        if task.assigned_to == user:
            self.update_task_status(task_status=TaskStatus.DONE, task=task)

        else:
            raise ValueError("This Task Does Not Belong to This User!")

    def set_freelancer_for_task(self, user: User, task: Task):
        self.dao.set_freelancer_for_task(user=user, task=task)

