from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from main.api.serializer.Registration.register_serializer import UserSerializer
from main.model.user_entity import User
from main.shared.initial_data.users.base_users import Users
from main.tests.prepare_test_env import PrepareTestEnv


class GetUserControllerTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = PrepareTestEnv().create_user(**Users.client)
        self.client.force_authenticate(user=self.user)
        self.get_user_url = reverse('get_user')

    def test_get_user(self):
        response = self.client.get(self.get_user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = UserSerializer(instance=self.user).data
        self.assertEqual(response.data, expected_data)
