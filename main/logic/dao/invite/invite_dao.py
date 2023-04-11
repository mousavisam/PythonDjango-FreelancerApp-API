from main.model.invite_entity import Invitation


class InviteDao:
    def create_invitation(self, sender, recipient_email):
        Invitation.objects.create(sender=sender, recipient_email=recipient_email)
