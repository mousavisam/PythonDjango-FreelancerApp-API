from typing import Dict

from django.core.exceptions import ObjectDoesNotExist

from main.logic.dao.rate.rate_dao import RateDao
from main.logic.user.user_logic import UserLogic
from main.model.user_entity import User


class RateLogic:

    def __init__(self):
        super().__init__()
        self.dao = RateDao()
        self.user_logic = UserLogic()

    def get_user_rate(self, user: User) -> Dict:
        return self.dao.get_user_rate(user=user)

    def create_rate(self, username, rate, request_user):
        user = self.user_logic.get_user_by_username(username)
        if user and user != request_user:
            self.dao.create_user(user, rate)

        else:
            raise ObjectDoesNotExist


