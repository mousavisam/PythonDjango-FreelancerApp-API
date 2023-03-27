import os

from ....model.profile_entity import Profile
from ....model.user_entity import User


class ProfileDao:

    def create_profile(self, **kwargs) -> None:
        Profile.objects.get_or_create(**kwargs)

    def update_profile(self, **kwargs) -> None:
        Profile.objects.filter(user=kwargs['user']).update(**kwargs)

    def update_profile_image(self, user: User, profile_image):
        profile = Profile.objects.filter(user=user).first()
        profile.personal_image = profile_image
        profile.save()

    def get_profile_by_user(self, user) -> Profile:
        return Profile.objects.filter(user=user).first()




