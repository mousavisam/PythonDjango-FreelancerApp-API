from typing import Tuple, Dict

from django.db.models import QuerySet

from main.logic.dao.profile.profile_dao import ProfileDao
from main.logic.rate.rate_logic import RateLogic
from main.logic.skill.skill_logic import SkillLogic
from main.model.profile_entity import Profile
from main.model.user_entity import User


class ProfileLogic:
    def __init__(self):
        super().__init__()
        self.dao = ProfileDao()
        self.rate_logic = RateLogic()
        self.skill_logic = SkillLogic()

    def create_profile(self, **kwargs) -> None:
        return self.dao.create_profile(**kwargs)

    def update_profile(self, **kwargs) -> None:
        return self.dao.update_profile(**kwargs)

    def update_profile_image(self, user: User, profile_image) -> None:
        return self.dao.update_profile_image(user=user, profile_image=profile_image)

    def get_profile_by_user(self, user: User) -> Profile:
        return self.dao.get_profile_by_user(user=user)

    def prepare_user_profile(self, user: User) -> Tuple[Profile, Dict, QuerySet]:
        user_profile = self.get_profile_by_user(user)
        avg_of_user_rate = self.rate_logic.get_user_rate(user)
        user_skills = self.skill_logic.get_user_skill(user)
        return user_profile, avg_of_user_rate, user_skills



