from rest_framework_simplejwt.tokens import RefreshToken

from ..dao.user.user_dao import UserDao
from ...model.user_entity import User


class UserLogic:
    def __init__(self):
        super().__init__()
        self.dao = UserDao()

    def get_user_by_id(self, user_id: int) -> User:
        return User.objects.filter(id=user_id).first()

    def get_user_by_username(self, username: str) -> User:
        return User.objects.filter(username=username).first()

    def create_refresh_token(self, user: User):
        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token
        return access_token, refresh_token

    def get_user_by_email(self, email: str) -> User:
        return User.objects.filter(email=email).first()

    def update_user_type(self, user, user_type) -> None:
        return self.dao.update_user_type(user=user, user_type=user_type)
