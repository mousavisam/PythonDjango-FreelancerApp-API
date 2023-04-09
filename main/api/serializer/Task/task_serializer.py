from rest_framework import serializers

from main.api.serializer.Category.category_serializer import CategoryAsTaskTag
from main.model.task_entity import Task


class CreateTaskSerializer(serializers.ModelSerializer):
    tags = serializers.ListField()

    class Meta:
        model = Task
        fields = ['title', 'deliver_time', 'description', 'tags']


class GetTaskSerializer(serializers.ModelSerializer):
    client = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['title', 'deliver_time', 'status', 'client', 'description', 'attachments', 'creation_time',
                  'description', 'tags']

    def get_client(self, obj):
        return obj.client.username

    def get_tags(self, obj):
        return CategoryAsTaskTag(obj.tags.all(), many=True).data


class TaskAttachmentFile(serializers.Serializer):
    task_id = serializers.IntegerField(min_value=1)
    attachment_file = serializers.FileField()


class UpdateTaskSerializer(serializers.Serializer):
    task_id = serializers.IntegerField(min_value=1)


class SearchTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title']
