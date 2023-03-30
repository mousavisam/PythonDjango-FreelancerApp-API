from django.db.models import QuerySet

from ....model.certificate_entity import Certificate
from ....model.user_entity import User


class CertificateDao:

    def create_certificate(self, **kwargs) -> None:
        Certificate.objects.create(**kwargs)

    def set_certificate_image(self, user: User, certificate_image):
        certificate = Certificate.objects.filter(user=user).first()
        certificate.image = certificate_image
        certificate.save()

    def get_certificate_by_user(self, user) -> QuerySet:
        return Certificate.objects.filter(user=user)
