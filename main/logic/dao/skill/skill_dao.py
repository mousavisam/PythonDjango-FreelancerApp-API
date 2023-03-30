from main.model.skill_entity import Skill
from main.model.user_entity import User


class SkillDao:

    def create_skill(self, **kwargs):
        Skill.objects.create(**kwargs)

    def get_user_skill(self, user: User):
        return Skill.objects.filter(user=user)

