from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from main.model.proposal_entity import Proposal
from main.shared.initial_data.category.generate_categories import GenerateCategories
from main.shared.initial_data.users.base_users import Users
from main.tests.prepare_test_env import PrepareTestEnv


class TestCreateTaskAndContract(APITestCase):

    def setUp(self):
        self.client_request = APIClient()
        self.freelancer_request = APIClient()
        self.client_user = PrepareTestEnv().create_user(**Users.client)
        self.freelancer_user = PrepareTestEnv().create_user(**Users.freelancer)
        GenerateCategories().add_new_categories()
        self.freelancer_request.force_authenticate(user=self.freelancer_user)
        self.client_request.force_authenticate(user=self.client_user)

        self.create_skill_url = reverse('create_skill')
        self.create_proposal_url = reverse('create_proposal')
        self.create_contract_url = reverse('create_contract')

    def test_create_task_and_contract_flow(self):
        task = PrepareTestEnv().create_task()
        proposal_data = {
            "delivery_time_in_day": 2147483647,
            "payment_amount": "27",
            "description": "string",
            "task_id": task.id
        }
        proposal_response = self.freelancer_request.post(self.create_proposal_url, data=proposal_data)
        self.assertEquals(proposal_response.status_code, status.HTTP_201_CREATED)

        contract_data = {
            "proposal": Proposal.objects.filter(id=1).first().id,
            "delivery_time_in_day": 156,
            "payment_amount": "36663184.8",
            "payment_type": "PER_HOUR",
            "start_time": "2023-04-13T19:05:59"
        }
        contract_response = self.client_request.post(self.create_contract_url, data=contract_data)
        self.assertEquals(contract_response.status_code, status.HTTP_201_CREATED)
