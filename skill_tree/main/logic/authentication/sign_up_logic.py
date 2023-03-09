from django.db.models import QuerySet

from ...model.user_entity import User


class SignUpLogic:

    def get_all_users(self) -> QuerySet:
        return User.objects.all()

    def insert_user(self, **kwargs) -> User:
        password = kwargs.pop('password')
        user = User.objects.create(**kwargs)
        user.set_password(password)
        return user
