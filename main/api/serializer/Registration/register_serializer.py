from rest_framework import serializers

from ....enum.user_status import UserType
from ....model.user_entity import User
from ....shared.utils import SkillTreeUtils


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'type']


class UpdateUserTypeSerializer(serializers.Serializer):
    user_type = serializers.ChoiceField(choices=UserType.choices)


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[SkillTreeUtils.validate_username], required=False)
    password = serializers.CharField(validators=[SkillTreeUtils.validate_password], required=False)
    first_name = serializers.CharField(required=False, max_length=150)
    last_name = serializers.CharField(required=False, max_length=150)
    email = serializers.EmailField(required=False, max_length=150)
    type = serializers.ChoiceField(choices=UserType.choices, required=False)

