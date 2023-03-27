from typing import Dict

from main.model.rate_entity import Rate
from main.model.user_entity import User
from django.db.models import Avg


class RateDao:

    def get_user_rate(self, user: User) -> Dict:
        return Rate.objects.filter(user=user).aggregate(rate=Avg('rate'))

    def create_user(self, user: User, rate: int):
        Rate.objects.create(user=user, rate=rate)