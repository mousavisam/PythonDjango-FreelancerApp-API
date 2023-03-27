from ....model.task_entity import Task


class TaskDao:

    def insert_task(self, **kwargs) -> None:
        Task.objects.create(**kwargs)

    def get_task_by_id(self, task_id: int) -> Task:
        return Task.objects.filter(id=task_id).first()

    def update_task_attachments(self, task: Task, filename: str) -> None:
        task.attachments = filename
        task.save()


