from django.urls import path

from ....api.controller.skill.skill_controller import SkillController

urlpatterns = [
    path('create/', SkillController.as_view({'post': 'post'}), name='create_skill'),
    path('', SkillController.as_view({'get': 'get'}), name='get_skill'),
]
