from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from ....api.serializer.certificate.certificate_serializer import InsertCertificateSerializer
from ....logic.certificate.certificate_logic import CertificateLogic
from ....shared.based_response.common_response import CreateResponse, ErrorResponse
from drf_spectacular.utils import extend_schema


class CertificateController(ViewSet):

    def __init__(self):
        super().__init__()
        self.certificate_logic = CertificateLogic()

    @extend_schema(
        request=InsertCertificateSerializer,
        tags=['Certificate'],
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
