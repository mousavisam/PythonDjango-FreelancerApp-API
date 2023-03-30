from django.db.models import QuerySet

from ...logic.dao.certificate.certificate_dao import CertificateDao
from ...model.user_entity import User
from ...model.certificate_entity import  Certificate


class CertificateLogic:
    def __init__(self):
        super().__init__()
        self.dao = CertificateDao()

    def create_certificate(self, **kwargs) -> None:
        return self.dao.create_certificate(**kwargs)

    def set_certificate_image(self, user: User, certificate_image) -> None:
        return self.dao.set_certificate_image(user=user, certificate_image=certificate_image)

    def get_certificate_by_user(self, user: User) -> QuerySet:
        return self.dao.get_certificate_by_user(user=user)
