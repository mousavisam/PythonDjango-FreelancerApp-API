from rest_framework import serializers

from ....model.profile_entity import Profile


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['count_of_served_tasks', 'count_of_requested_tasks', 'status']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('personal_image',)


class GetProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['count_of_served_tasks', 'count_of_requested_tasks', 'status', 'first_name', 'last_name', 'email',
                  'username', 'personal_image']

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_email(self, obj):
        return obj.user.email

    def get_username(self, obj):
        return obj.user.username
