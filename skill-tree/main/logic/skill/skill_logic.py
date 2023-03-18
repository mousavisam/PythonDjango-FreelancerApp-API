from main.enum.level_type import LevelType
from main.logic.category.category_logic import CategoryLogic
from main.logic.dao.skill.skill_dao import SkillDao
from main.model.user_entity import User

from django.core.exceptions import ObjectDoesNotExist


class SkillLogic:
    def __init__(self):
        super().__init__()
        self.category_logic = CategoryLogic()
        self.dao = SkillDao()

    def create_skill(self, title: str, level: LevelType, user: User):
        category = self.category_logic.get_category_by_title(title)
        if category:
            self.dao.create_skill(category=category, level=level, user=user)
        else:
            raise ObjectDoesNotExist
