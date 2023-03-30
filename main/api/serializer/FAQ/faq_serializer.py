from rest_framework import serializers

from main.model.faq_entity import FAQ


class GetFAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = ['question', 'answer']