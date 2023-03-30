from ...logic.user.user_logic import UserLogic


class LoginLogic:

    def __init__(self):
        self.user_logic = UserLogic()

    def login(self, username: str, password: str):
        user = self.user_logic.get_user_by_username(username)
        user_type = user.type
        if user:
            if user.check_password(password):
                access_token, refresh_token = self.user_logic.create_refresh_token(user)
                return {'access_token': str(access_token), 'refresh_token': str(refresh_token), 'user_type': user_type}
            else:
                raise ValueError("Password is incorrect")
            # ValueError display with 500 status code
        else:
            raise ValueError("User Does Not Exist!")
