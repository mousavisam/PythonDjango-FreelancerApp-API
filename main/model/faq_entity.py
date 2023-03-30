from django.db import models


class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    creation_time = models.DateTimeField(auto_now=True)