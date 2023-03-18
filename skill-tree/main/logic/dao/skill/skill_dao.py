from main.model.skill_entity import Skill


class SkillDao:

    def create_skill(self, **kwargs):
        Skill.objects.create(**kwargs)
