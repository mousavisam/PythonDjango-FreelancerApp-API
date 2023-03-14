from django.db import models
from ..model.user_entity import User
from ..model.skill_entity import Skill
from ..enum.profile_status import ProfileStatus


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now=True)
    skill = models.ForeignKey(Skill, on_delete=models.DO_NOTHING,blank=True, null=True)
    count_of_served_tasks = models.IntegerField()
    count_of_requested_tasks = models.IntegerField()
    joined_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=ProfileStatus.choices)
    # personal_image = models.ImageField(upload_to='images')
