from django.db import models
from ..model.skill_entity import Skill
from ..model.user_entity import User
from ..shared.utils import SkillTreeUtils


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    earned_date = models.DateTimeField(auto_now=False)
    image = models.ImageField(upload_to=SkillTreeUtils.get_certificate_user_file_path)
    link = models.CharField(max_length=128, unique=True, blank=True, null=True)
