from django.core.mail import send_mail

from main.logic.dao.invite.invite_dao import InviteDao
from main.model.vo.invite.invite_vo import InviteVo


class InviteLogic:
    def __init__(self):
        super().__init__()
        self.dao = InviteDao()

    def send_invitation_email(self, recipient_email, user):
        send_mail("Invitation Link", message=InviteVo.message, from_email=user.email, recipient_list=[recipient_email])
        self.dao.create_invitation(sender=user, recipient_email=recipient_email)
