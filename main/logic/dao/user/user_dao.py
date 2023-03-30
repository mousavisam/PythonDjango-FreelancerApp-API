from main.enum.user_status import UserType
from main.model.user_entity import User


class UserDao:

    def update_user_type(self, user: User, user_type: UserType):
        user.type = user_type
        user.save()
