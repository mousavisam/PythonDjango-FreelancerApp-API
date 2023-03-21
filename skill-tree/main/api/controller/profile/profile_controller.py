from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema

from main.api.serializer.Profile.profile_serializer import UpdateProfileSerializer, ImageSerializer
from main.logic.profile.profile_logic import ProfileLogic
from main.shared.based_response.common_response import UpdateResponse


class ProfileController(ViewSet):

    def __init__(self):
        super().__init__()
        self.profile_logic = ProfileLogic()

    @extend_schema(
        request=UpdateProfileSerializer,
        tags=['profile'],
        responses={200: str},
    )
    def patch(self, request: Request):
        serializer = UpdateProfileSerializer(data=request.data)
        if serializer.is_valid():
            count_of_served_tasks = serializer.validated_data.get("count_of_served_tasks", None)
            count_of_requested_tasks = serializer.validated_data.get("count_of_requested_tasks", None)
            user_status = serializer.validated_data.get("status", None)
            self.profile_logic.update_profile(count_of_requested_tasks=count_of_requested_tasks,
                                              count_of_served_tasks=count_of_served_tasks, status=user_status,
                                              user=request.user)

            return UpdateResponse()

        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'personal_image': {
                        'type': 'string',
                        'format': 'binary'
                    }
                }
            }},
        tags=['profile'],
        responses={200: str},
    )
    def set_profile_image(self, request: Request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            profile_image = serializer.validated_data.get("personal_image", None)
            self.profile_logic.update_profile_image(profile_image=profile_image, user=request.user)

            return UpdateResponse()

        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
