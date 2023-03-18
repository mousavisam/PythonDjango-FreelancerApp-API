from django.db import models
from ..model.user_entity import User
from ..model.skill_entity import Skill


class Test(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    skill = models.ForeignKey(Skill, on_delete=models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    score = models.DecimalField(max_digits=5, decimal_places=3)
    date = models.DateField(auto_now=False)

