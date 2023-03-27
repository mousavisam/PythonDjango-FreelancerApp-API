from ...logic.dao.certificate.certificate_dao import CertificateDao
from ...model.certificate_entity import Certificate


class CertificateLogic:
    def __init__(self):
        super().__init__()
        self.dao = CertificateDao()

    def create_certificate(self, **kwargs) -> None:
        return self.dao.create_certificate(**kwargs)
