from django.db.models import QuerySet

from main.enum.task_status import TaskStatus
from main.logic.category.category_logic import CategoryLogic
from main.logic.dao.task.task_dao import TaskDao
from main.logic.skill.skill_logic import SkillLogic
from main.model.task_entity import Task
from main.model.user_entity import User


class TaskLogic:

    def __init__(self):
        super().__init__()
        self.dao = TaskDao()
        self.category_logic = CategoryLogic()
        self.skill_logic = SkillLogic()

    def insert_task(self, **kwargs):
        list_of_categories = list()
        for tag in kwargs['tags']:
            category = self.category_logic.get_category_by_title(title=tag)
            list_of_categories.append(category)
        kwargs.pop('tags')
        kwargs['tags'] = list_of_categories
        kwargs['status'] = TaskStatus.UNASSIGNED
        task = self.dao.insert_task(**kwargs)
        related_tasks = self.get_task_by_multiple_tags(task=task)
        return related_tasks

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

    def get_task_by_tag(self, tag: str) -> QuerySet:
        tasks = self.dao.get_task_by_tag(tag)
        return tasks

    def get_task_by_multiple_tags(self, task):
        return self.dao.get_task_by_multiple_tags(task)

    def get_task_by_title(self, title: str) -> QuerySet:
        return self.dao.get_task_by_title(title=title)

    def get_tasks_related_to_user_skills(self, user: User):
        set_of_tasks = set()
        user_skills = self.skill_logic.get_user_skill(user=user)
        for skill in user_skills:
            tasks = self.get_task_by_tag(tag=skill.category.title)
            for task in tasks:
                if task.assigned_to is None:
                    set_of_tasks.add(task)

        return set_of_tasks

    def get_all_tasks_by_client(self, client):
        return self.dao.get_all_tasks_by_client(client=client)

    def get_all_tasks_by_freelancer(self, freelancer):
        return self.dao.get_all_tasks_by_freelancer(freelancer=freelancer)
