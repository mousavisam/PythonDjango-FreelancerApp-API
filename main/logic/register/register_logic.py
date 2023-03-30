from typing import Dict

from django.db.models import QuerySet

from ..profile.profile_logic import ProfileLogic
from ..user.user_logic import UserLogic
from ...enum.profile_status import ProfileStatus
from ...model.user_entity import User


class RegisterLogic:
    def __init__(self) -> None:
        super().__init__()
        self.profile_logic = ProfileLogic()
        self.user_logic = UserLogic()

    def get_all_users(self) -> QuerySet:
        return User.objects.all()

    def insert_user(self, **kwargs) -> int:
        password = kwargs.pop('password')
        user = User.objects.create(**kwargs)
        user.set_password(password)
        user.save()
        self.profile_logic.create_profile(user=user, count_of_served_tasks=0, count_of_requested_tasks=0,
                                          status=ProfileStatus.FREE)
        return user

    def google_signin(self, **kwargs) -> Dict:
        user = self.user_logic.get_user_by_email(kwargs['email'])

        if user:

            access_token, refresh_token = self.user_logic.create_refresh_token(user)
            return {'access_token': str(access_token), 'refresh_token': str(refresh_token)}
        else:
            user = User.objects.create(**kwargs)
            user.save()
            self.profile_logic.create_profile(user=user, count_of_served_tasks=0, count_of_requested_tasks=0,
                                              status=ProfileStatus.FREE)

            access_token, refresh_token = self.user_logic.create_refresh_token(user)
            return {'access_token': str(access_token), 'refresh_token': str(refresh_token)}


