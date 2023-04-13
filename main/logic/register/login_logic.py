from datetime import datetime

from ..user_session.user_session_logic import UserSessionLogic
from ...logic.user.user_logic import UserLogic


class LoginLogic:

    def __init__(self):
        self.user_logic = UserLogic()
        self.user_session_logic = UserSessionLogic()

    def login(self, username: str, password: str):
        user = self.user_logic.get_user_by_username(username)
        if user:
            user_type = user.type
            if user.check_password(password):
                access_token, refresh_token = self.user_logic.create_refresh_token(user)
                self.user_session_logic.insert_user_session(user=user, start_date=datetime.now())
                return {'access_token': str(access_token), 'refresh_token': str(refresh_token), 'user_type': user_type}
            else:
                raise ValueError("Password is incorrect")
            # ValueError display with 500 status code
        else:
            raise ValueError("User Does Not Exist!")
