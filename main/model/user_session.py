from django.conf import settings
from django.db import models
from django.utils import timezone


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session_start = models.DateTimeField()
    session_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.session_start})"
