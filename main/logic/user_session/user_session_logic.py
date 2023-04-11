from main.logic.dao.user_session.user_session_dao import UserSessionDao


class UserSessionLogic:

    def __init__(self):
        super().__init__()

        self.dao = UserSessionDao()

    def insert_user_session(self, user, start_date):
        self.dao.insert_user_session(user=user, start_date=start_date)

    def get_last_user_session(self, user):
        return self.dao.get_last_user_session(user=user)

    def get_all_sessions_by_user(self, user):
        return self.dao.get_all_sessions_by_user(user=user)
