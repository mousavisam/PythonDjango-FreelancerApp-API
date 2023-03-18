from django.urls import path

from main.api.controller.skill.skill_controller import SkillController

urlpatterns = [
    path('create/', SkillController.as_view({'post': 'post'}), name='skill'),
]
