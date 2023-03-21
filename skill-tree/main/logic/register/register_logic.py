from django.db.models import QuerySet

from ..profile.profile_logic import ProfileLogic
from ...enum.profile_status import ProfileStatus
from ...model.user_entity import User


class RegisterLogic:
    def __init__(self) -> None:
        super().__init__()
        self.profile_logic = ProfileLogic()

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

