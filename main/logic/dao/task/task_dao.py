from ....enum.task_status import TaskStatus
from ....model.task_entity import Task
from ....model.user_entity import User


class TaskDao:

    def insert_task(self, **kwargs) -> None:
        Task.objects.create(**kwargs)

    def get_task_by_id(self, task_id: int) -> Task:
        return Task.objects.filter(id=task_id).first()

    def update_task_attachments(self, task: Task, filename: str) -> None:
        task.attachments = filename
        task.save()

    def update_task_status(self, task: Task, task_status: TaskStatus) -> None:
        task.status = task_status
        task.save()

    def set_freelancer_for_task(self, user: User, task: Task) -> None:
        task.assigned_to = user
        task.save()



