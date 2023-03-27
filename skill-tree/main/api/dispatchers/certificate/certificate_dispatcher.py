from django.urls import path

from ....api.controller.certificate.certificate_controller import CertificateController

urlpatterns = [
    path('create/', CertificateController.as_view({'post': 'post'}), name='create_certificate'),
]
