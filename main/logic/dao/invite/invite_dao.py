from main.model.invite_entity import Invitation


class InviteDao:
    def create_invitation(self, **kwargs):
        Invitation.objects.create(kwargs)