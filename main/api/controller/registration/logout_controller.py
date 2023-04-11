from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from main.api.serializer.Registration.logout_serializer import LogoutSerializer
from main.logic.register.logout_logic import LogoutLogic
from main.shared.based_response.common_response import ErrorResponse


class LogoutController(ViewSet):

    def __init__(self):
        super().__init__()
        self.logout_logic = LogoutLogic()

    @extend_schema(
        request=LogoutSerializer,
        tags=["Auth"],
        responses={200: None},
    )
    def post(self, request: Request):
        serializer = LogoutSerializer(data=request.data)
        if serializer.is_valid():
            refresh_token = serializer.validated_data.get('refresh_token', None)
            self.logout_logic.logout(refresh_token=refresh_token, user=request.user)

            return Response({"message": "You have been successfully logged out."}, status=status.HTTP_200_OK)

        else:
            return ErrorResponse(message=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)
