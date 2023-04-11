import datetime

from rest_framework_simplejwt.tokens import RefreshToken

from main.logic.user_session.user_session_logic import UserSessionLogic


class LogoutLogic:
    def __init__(self):
        super().__init__()
        self.user_session_logic = UserSessionLogic()

    def logout(self, refresh_token, user):
        token = RefreshToken(refresh_token)
        token.blacklist()
        session = self.user_session_logic.get_last_user_session(user=user)
        session.session_end = datetime.datetime.now()
        session.save()
