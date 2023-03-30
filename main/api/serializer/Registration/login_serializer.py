from rest_framework import serializers

from ....shared.utils import SkillTreeUtils


class LoginRequest(serializers.Serializer):

    username = serializers.CharField(validators=[SkillTreeUtils.validate_username], required=True)
    password = serializers.CharField(validators=[SkillTreeUtils.validate_password], required=True)


