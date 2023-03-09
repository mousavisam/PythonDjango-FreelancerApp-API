from rest_framework import serializers

from ....model.user_entity import User


class UserSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=20)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)


class UserSignUpRequest(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'type', 'creation_time']



