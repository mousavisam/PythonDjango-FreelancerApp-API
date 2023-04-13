from main.model.user_session import UserSession


class UserSessionDao:

    def insert_user_session(self, user, start_date):
        UserSession.objects.create(user=user, session_start=start_date)

    def get_last_user_session(self, user):
        return UserSession.objects.filter(user=user).order_by('-session_start').first()

    def get_all_sessions_by_user(self, user):
        return UserSession.objects.filter(user=user).order_by('-session_start')
