from main.enum.user_status import UserType
from main.logic.task.task_logic import TaskLogic
from main.logic.user_session.user_session_logic import UserSessionLogic
from main.model.user_entity import User


class ReportLogic:
    def __init__(self):
        super().__init__()
        self.task_logic = TaskLogic()
        self.user_session = UserSessionLogic()

    def generate_user_report(self, user: User):
        user_sessions = self.user_session.get_all_sessions_by_user(user=user)
        count_of_requested_tasks, count_of_served_tasks = 0, 0

        if user.type == UserType.CLIENT:
            count_of_requested_tasks = self.task_logic.get_all_tasks_by_client(client=user)

        elif user.type == UserType.FREELANCER:
            count_of_served_tasks = self.task_logic.get_all_tasks_by_freelancer(freelancer=user)

        return user_sessions, count_of_requested_tasks, count_of_served_tasks


