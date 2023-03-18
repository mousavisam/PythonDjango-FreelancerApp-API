from django.core.validators import MinValueValidator
from django.db import models
from ..model.user_entity import User
from ..model.skill_entity import Skill
from ..enum.profile_status import ProfileStatus
from main.shared.utils import SkillTreeUtils


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='profile')
    count_of_served_tasks = models.IntegerField(validators=[MinValueValidator(0.0)])
    count_of_requested_tasks = models.IntegerField(validators=[MinValueValidator(0.0)])
    joined_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=ProfileStatus.choices)
    personal_image = models.ImageField(upload_to=SkillTreeUtils.get_profile_user_file_path, null=True, blank=True)

    def __str__(self):
        return self.user.username
