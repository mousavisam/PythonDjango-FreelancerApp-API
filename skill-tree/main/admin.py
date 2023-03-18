from django.contrib import admin

from .model.category_entity import Category
from .model.profile_entity import Profile
from .model.skill_entity import Skill
from .model.user_entity import User


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Profile)

