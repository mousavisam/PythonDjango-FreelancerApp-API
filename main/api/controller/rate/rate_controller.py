from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from main.api.serializer.Rate.rate_serializer import CreateRateSerializer
from main.logic.rate.rate_logic import RateLogic
from main.shared.based_response.common_response import CreateResponse, ErrorResponse


class RateController(ViewSet):

    def __init__(self):
        super().__init__()
        self.rate_logic = RateLogic()

    @extend_schema(
        request=CreateRateSerializer,
        tags=['Rate'],
        responses={201: None},
    )
    def post(self, request: Request):

        serializer = CreateRateSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username", None)
            rate = serializer.validated_data.get("rate", None)
            try:
                self.rate_logic.create_rate(username=username, rate=rate, request_user=request.user)
                return CreateResponse()
            except Exception as e:
                return ErrorResponse(message=str(e), status_code=status.HTTP_406_NOT_ACCEPTABLE)

        else:
            return ErrorResponse(message=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)


