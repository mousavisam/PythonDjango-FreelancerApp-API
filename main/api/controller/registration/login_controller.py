from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from drf_spectacular.utils import extend_schema

from ...serializer.Registration.register_serializer import UpdateUserTypeSerializer, UserSerializer
from ....api.serializer.Registration.login_serializer import LoginRequest
from ....logic.register.login_logic import LoginLogic
from ....logic.user.user_logic import UserLogic
from ....shared.based_response.common_response import UpdateResponse, ErrorResponse


class LoginController(ViewSet):
    permission_classes = [AllowAny]

    def __init__(self):
        super().__init__()
        self.login_logic = LoginLogic()
        self.user_logic = UserLogic()

    @extend_schema(
        request=LoginRequest,
        tags=["Auth"],
        responses={201: dict},
    )
    def post(self, request: Request):
        serializer = LoginRequest(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username", None)
            password = serializer.validated_data.get("password", None)
            response = self.login_logic.login(username, password)

            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[UpdateUserTypeSerializer],
        tags=["Auth"],
        responses={202: None},
    )
    def update_user_type(self, request: Request):

        serializer = UpdateUserTypeSerializer(data=request.query_params)
        if serializer.is_valid():
            user_type = serializer.validated_data.get('user_type')
            self.user_logic.update_user_type(user=request.user, user_type=user_type)
            return UpdateResponse()
        else:
            return ErrorResponse(message=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)


class GetUserController(ViewSet):
    @extend_schema(
        tags=["Auth"],
        responses={200: UserSerializer},
    )
    def get_user(self, request: Request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

