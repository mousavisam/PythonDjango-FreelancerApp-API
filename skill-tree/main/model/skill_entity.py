from django.db import models
from ..model.category_entity import Category
from ..enum.level_type import LevelType
from ..model.user_entity import User


class Skill(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    level = models.CharField(max_length=20, choices=LevelType.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
