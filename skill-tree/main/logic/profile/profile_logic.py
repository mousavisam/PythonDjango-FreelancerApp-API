from main.logic.dao.profile.profile_dao import ProfileDao
from main.model.profile_entity import Profile
from main.model.user_entity import User


class ProfileLogic:
    def __init__(self):
        super().__init__()
        self.dao = ProfileDao()

    def create_profile(self, **kwargs) -> None:
        return self.dao.create_profile(**kwargs)

    def update_profile(self, **kwargs) -> None:
        return self.dao.update_profile(**kwargs)

    def update_profile_image(self, user: User, profile_image) -> None:
        return self.dao.update_profile_image(user=user, profile_image=profile_image)
