from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist
from main.api.serializer.Skill.skill_serializer import CreateSkillSerializer
from main.logic.skill.skill_logic import SkillLogic
from drf_spectacular.utils import extend_schema


class SkillController(ViewSet):

    def __init__(self):
        super().__init__()
        self.skill_logic = SkillLogic()

    @extend_schema(
        request=CreateSkillSerializer,
        tags=['Skill'],
        responses={201: None},
    )
    def post(self, request: Request):
        serializer = CreateSkillSerializer(data=request.data)
        if serializer.is_valid():

            skill_name = serializer.validated_data.get("skill_name", None)
            level_type = serializer.validated_data.get("level", None)
            try:
                self.skill_logic.create_skill(title=skill_name, level=level_type, user=request.user)
                return Response(status=status.HTTP_201_CREATED)

            except ObjectDoesNotExist:
                return Response(data="Category does not exist", status=status.HTTP_404_NOT_FOUND)

        else:
            return Response(str(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
