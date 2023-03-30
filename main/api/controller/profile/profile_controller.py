from typing import Dict

from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema

from main.api.serializer.Profile.profile_serializer import UpdateProfileSerializer, ImageSerializer, \
    GetProfileSerializer
from main.api.serializer.Skill.skill_serializer import GetSkillSerializer
from main.api.serializer.certificate.certificate_serializer import GetCertificateSerializer
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

    @extend_schema(
        tags=['profile'],
        responses={200: Dict},
    )
    def get(self, request: Request):
        profile, rate, skill, certificates = self.profile_logic.prepare_user_profile(user=request.user)
        profile_serializer = GetProfileSerializer(profile)
        skill_serializer = GetSkillSerializer(skill, many=True)
        certificate_serializer = GetCertificateSerializer(certificates, many=True)
        profile_data = profile_serializer.data
        if certificate_serializer.data:
            profile_data['certificates'] = list()
            for certificate in certificate_serializer.data:
                profile_data['certificates'].append(dict(certificate))

        if skill_serializer.data:
            profile_data['skill'] = list()
            for skill in skill_serializer.data:
                profile_data['skill'].append(dict(skill))

        profile_data.update(rate)

        return Response(profile_data, status=status.HTTP_200_OK)
