from rest_framework import serializers

from main.model.user_session import UserSession


class UserSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = ['session_start', 'session_end']