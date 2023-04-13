from typing import Dict

from rest_framework.test import APIClient
from django.urls import reverse

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
        data = {
            'title': 'Test Task',
            'deliver_time': '2023-04-12',
            'description': 'This is a tests task.',
            'tags': ['python', 'php'],
            'client': User.objects.filter(username='user10').first()
        }
        return Task.objects.create(**data)
