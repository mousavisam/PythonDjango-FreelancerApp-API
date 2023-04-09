from rest_framework import serializers


class BrowseSerializer(serializers.Serializer):

    keyword = serializers.CharField(max_length=30, required=True)