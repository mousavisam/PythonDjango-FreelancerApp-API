from rest_framework import serializers

from main.model.task_entity import Task


class CreateTaskSerializer(serializers.ModelSerializer):
    service_category = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['title', 'deliver_time', 'status', 'description']

    def get_service_category(self):
        return
