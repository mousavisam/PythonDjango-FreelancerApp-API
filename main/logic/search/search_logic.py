from typing import Tuple

from django.db.models import QuerySet

from main.logic.task.task_logic import TaskLogic
from main.logic.user.user_logic import UserLogic


class SearchLogic:

    def __init__(self):
        super().__init__()
        self.user_logic = UserLogic()
        self.task_logic = TaskLogic()

    def search_by_keyword(self, keyword: str) -> Tuple[QuerySet, set]:
        users = self.user_logic.search_user_by_username(username=keyword)
        tasks_by_title = self.task_logic.get_task_by_title(title=keyword)
        title_tasks_set = {task for task in tasks_by_title}
        tasks_by_tag = self.task_logic.get_task_by_tag(tag=keyword)
        tag_tasks_set = {task for task in tasks_by_tag}
        tasks = title_tasks_set.union(tag_tasks_set)

        return users, tasks

