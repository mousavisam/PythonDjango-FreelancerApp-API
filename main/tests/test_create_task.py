from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from main.shared.initial_data.category.generate_categories import GenerateCategories
from main.tests.prepare_test_env import PrepareTestEnv


class TaskControllerTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = PrepareTestEnv().create_user()
        GenerateCategories().add_new_categories()
        self.client.force_authenticate(user=self.user)
        self.create_task_url = reverse('create_task')

    def test_create_task_with_valid_data(self):
        data = {
            'title': 'Test Task',
            'deliver_time': '2023-04-12',
            'description': 'This is a tests task.',
            'tags': ['python', 'php']
        }
        response = self.client.post(self.create_task_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual([], response.data)

    #
    def test_create_task_with_invalid_data(self):
        data = {
            'title': '',
            'deliver_time': '2023-04-12T08:00:00Z',
            'description': 'This is a tests task.',
            'tags': ['tag1', 'tag2']
        }
        response = self.client.post(self.create_task_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
