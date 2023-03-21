from rest_framework import serializers

from main.model.profile_entity import Profile


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['count_of_served_tasks', 'count_of_requested_tasks', 'status']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('personal_image',)
