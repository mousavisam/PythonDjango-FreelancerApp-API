from rest_framework import serializers

from main.enum.task_status import TaskStatus
from main.model.task_entity import Task


class CreateTaskSerializer(serializers.ModelSerializer):
    service_category = serializers.CharField(max_length=150)

    class Meta:
        model = Task
        fields = ['title', 'deliver_time', 'description', 'service_category']


class TaskAttachmentFile(serializers.Serializer):
    task_id = serializers.IntegerField(min_value=1)
    attachment_file = serializers.FileField()


class UpdateTaskSerializer(serializers.Serializer):
    task_id = serializers.IntegerField(min_value=1)