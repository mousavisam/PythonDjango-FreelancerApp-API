from django.db.models import QuerySet

from main.enum.user_status import UserType
from main.model.user_entity import User


class UserDao:

    def update_user_type(self, user: User, user_type: UserType):
        user.type = user_type
        user.save()

    def search_user_by_username(self, username: str) -> QuerySet:
        return User.objects.filter(username__icontains=username)
