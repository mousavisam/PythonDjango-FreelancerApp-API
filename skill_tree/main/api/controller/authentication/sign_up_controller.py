from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ...serializer.authentication.sign_up_serializer import UserSignUpRequest, UserSerializer
from ....logic.authentication.sign_up_logic import SignUpLogic


class SignUpController(ViewSet):
    permission_classes = [AllowAny]

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.sign_up_logic = SignUpLogic()

    @extend_schema(
        tags=["Auth"],

        responses={200: UserSerializer},
    )
    def retrieve(self, request: Request):
        users = self.sign_up_logic.get_all_users()

        serialized_response = UserSerializer(users, many=True)
        return Response(data=serialized_response.data, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=UserSignUpRequest,
        tags=["Auth"],

        responses={201: int},
    )
    def post(self, request: Request):
        serializer = UserSignUpRequest(data=request.data)
        if serializer.is_valid():
            try:
                username = serializer.validated_data.get('username')
                password = serializer.validated_data.get('password')
                email = serializer.validated_data.get('email')
                first_name = serializer.validated_data.get('first_name')
                last_name = serializer.validated_data.get('last_name')
                user_type = serializer.validated_data.get('type')
                creation_time = serializer.validated_data.get('creation_time')
                self.sign_up_logic.insert_user(username=username, password=password,
                                                          email=email, first_name=first_name,
                                                          last_name=last_name, type=user_type, creation_time=creation_time)
                return Response(data="You signed up successfully", status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
