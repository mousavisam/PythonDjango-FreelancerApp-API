from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers


class CreateRateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)
    rate = serializers.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
