from rest_framework.test import APIClient

from main.enum.task_status import TaskStatus
from main.logic.category.category_logic import CategoryLogic
from main.model.task_entity import Task
from main.model.user_entity import User


class PrepareTestEnv:
    def setUp(self):
        self.client = APIClient()
        self.user = self.create_user()
        self.client.force_authenticate(user=self.user)

    def create_user(self, **kwargs):
        password = kwargs.pop('password')
        user = User.objects.create(**kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_task(self):
        list_of_categories = list()
        data = {
            'title': 'Test Task',
            'deliver_time': '2023-04-12',
            'description': 'This is a tests task.',
            'tags': ['python', 'php'],
            'client': User.objects.filter(username='user10').first()
        }
        for tag in data['tags']:
            category = CategoryLogic().get_category_by_title(title=tag)
            list_of_categories.append(category)
        data.pop('tags')
        data['status'] = TaskStatus.UNASSIGNED
        task = Task.objects.create(**data)
        task.tags.set(list_of_categories)
        task.save()

        return task
