from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from ....api.serializer.certificate.certificate_serializer import InsertCertificateSerializer, \
    CertificateImageSerializer, GetCertificateSerializer
from ....logic.certificate.certificate_logic import CertificateLogic
from ....shared.based_response.common_response import CreateResponse, ErrorResponse, UpdateResponse
from drf_spectacular.utils import extend_schema


class CertificateController(ViewSet):

    def __init__(self):
        super().__init__()
        self.certificate_logic = CertificateLogic()

    @extend_schema(
        request=InsertCertificateSerializer,
        tags=['certificate'],
        responses={201: None},
    )
    def post(self, request: Request):
        serializer = InsertCertificateSerializer(data=request.data)
        if serializer.is_valid():

            title = serializer.validated_data.get("title", None)
            description = serializer.validated_data.get("description", None)
            earned_date = serializer.validated_data.get("earned_date", None)
            link = serializer.validated_data.get("link", None)
            try:
                self.certificate_logic.create_certificate(title=title, description=description, earned_date=earned_date,
                                                          link=link, user=request.user)
                return CreateResponse()

            except Exception as e:
                return Response(data=str(e), status=status.HTTP_404_NOT_FOUND)

        else:
            ErrorResponse(message=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'image': {
                        'type': 'string',
                        'format': 'binary'
                    }
                }
            }},
        tags=['certificate'],
        responses={200: str},
    )
    def patch(self, request: Request):
        serializer = CertificateImageSerializer(data=request.data)
        if serializer.is_valid():
            certificate_image = serializer.validated_data.get("image", None)
            self.certificate_logic.set_certificate_image(certificate_image=certificate_image, user=request.user)

            return UpdateResponse()

        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=['certificate'],
        responses={200: GetCertificateSerializer},
    )
    def get(self, request: Request):
        user_certificates = self.certificate_logic.get_certificate_by_user(user=request.user)

        serializer = GetCertificateSerializer(user_certificates, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
