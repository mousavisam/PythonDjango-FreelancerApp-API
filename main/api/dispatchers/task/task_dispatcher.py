from django.urls import path

from main.api.controller.task.task_controller import TaskController

urlpatterns = [
    path('create/', TaskController.as_view({'post': 'post'}), name='create_task'),
    path('set_attachment_file/', TaskController.as_view({'patch': 'set_attachment_file'}), name='set_attachment_file'),
    path('', TaskController.as_view({'patch': 'patch'}), name='update_task_status'),
]
