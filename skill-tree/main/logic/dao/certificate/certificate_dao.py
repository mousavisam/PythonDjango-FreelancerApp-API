from ....model.certificate_entity import Certificate


class CertificateDao:

    def create_certificate(self, **kwargs) -> None:
        Certificate.objects.create(**kwargs)
