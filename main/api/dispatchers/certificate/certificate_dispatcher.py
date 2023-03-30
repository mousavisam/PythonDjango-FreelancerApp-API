from django.urls import path

from ....api.controller.certificate.certificate_controller import CertificateController

urlpatterns = [
    path('create/', CertificateController.as_view({'post': 'post'}), name='create_certificate'),
    path('', CertificateController.as_view({'patch': 'patch'}), name='set_image'),
    path('', CertificateController.as_view({'get': 'get'}), name='get_certificate'),
]
