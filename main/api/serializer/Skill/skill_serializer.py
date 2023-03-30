from rest_framework import serializers

from ....enum.level_type import LevelType
from ....model.skill_entity import Skill


class CreateSkillSerializer(serializers.Serializer):
    skill_name = serializers.CharField(max_length=100)
    level = serializers.ChoiceField(choices=LevelType.choices)


class GetSkillSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = ['category', 'level']

    def get_category(self, obj):
        return obj.category.title

