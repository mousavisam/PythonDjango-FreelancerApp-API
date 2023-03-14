from rest_framework import serializers

from ....model.user_entity import User
from ....shared.utils import SkillTreeUtils


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[SkillTreeUtils.validate_username])
    password = serializers.CharField(validators=[SkillTreeUtils.validate_password])

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'type']
