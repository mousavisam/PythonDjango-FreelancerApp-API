from django.db import models

from main.model.user_entity import User


class Invitation(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient_email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} invited {self.recipient_email}"
