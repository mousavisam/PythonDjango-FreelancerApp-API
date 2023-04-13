from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from main.shared.initial_data.category.generate_categories import GenerateCategories
from main.tests.prepare_test_env import PrepareTestEnv


class CreateSkillTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = PrepareTestEnv().create_user()
        GenerateCategories().add_new_categories()
        self.client.force_authenticate(user=self.user)
        self.create_skill_url = reverse('create_skill')

    def test_create_skill_with_valid_data(self):

        data = {
            'skill_name': 'php',
            'level': 'JUNIOR'
        }
        response = self.client.post(self.create_skill_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_skill_with_invalid_data(self):
        url = '/api/skills/'
        data = {
            'skill_name': '',
            'level': 'Intermediate'
        }
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST


    def test_get_user_skills(self):
        url = '/api/skills/'
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 0

        # create a skill for the authenticated user
        data = {
            'skill_name': 'Test Skill',
            'level': 'Intermediate'
        }
        authenticated_client.post(url, data, format='json')

        # verify that the skill was added to the user's skills
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['skill_name'] == 'Test Skill'
        assert response.data[0]['level'] == 'Intermediate'