from django.db import models
from ..model.skill_entity import Skill
from ..model.user_entity import User


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    skill = models.ForeignKey(Skill, on_delete=models.DO_NOTHING,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    earned_date = models.DateTimeField(auto_now=False)
    # image = models.ImageField(upload_to='images')
    # link = models.URLField(
    #     _("Link Number"),
    #     max_length=128,
    #     db_index=True,
    #     unique=True,
    #     blank=True
    # )
