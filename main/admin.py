from django.contrib import admin

from .model.category_entity import Category
from .model.profile_entity import Profile
from .model.proposal_entity import Proposal
from .model.rate_entity import Rate
from .model.skill_entity import Skill
from .model.user_entity import User


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(Proposal)
admin.site.register(Rate)


