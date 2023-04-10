from rest_framework import serializers


class SendInvitationSerializer(serializers.Serializer):
    recipient_email = serializers.EmailField()
    # message = serializers.CharField()

