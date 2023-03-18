from rest_framework import serializers

from main.enum.level_type import LevelType


class CreateSkillSerializer(serializers.Serializer):
    skill_name = serializers.CharField(max_length=100)
    level = serializers.ChoiceField(choices=LevelType.choices)