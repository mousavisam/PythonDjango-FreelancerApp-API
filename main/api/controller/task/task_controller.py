from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework import status
from drf_spectacular.utils import extend_schema

from ....api.serializer.Task.task_serializer import CreateTaskSerializer, TaskAttachmentFile, UpdateTaskSerializer, \
    GetTaskSerializer
from ....logic.task.task_logic import TaskLogic
from ....model.vo.task.task_vo import TaskVO
from ....shared.based_response.common_response import CreateResponse, ErrorResponse, UpdateResponse


class TaskController(ViewSet):

    def __init__(self):
        super().__init__()
        self.task_logic = TaskLogic()

    @extend_schema(
        request=CreateTaskSerializer,
        tags=['Task'],
        responses={201: str},
    )
    def post(self, request: Request):
        serializer = CreateTaskSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get(TaskVO.title, None)
            deliver_time = serializer.validated_data.get(TaskVO.deliver_time, None)
            description = serializer.validated_data.get(TaskVO.description, None)
            tags = serializer.validated_data.get('tags', None)
            try:
                self.task_logic.insert_task(title=title, deliver_time=deliver_time, description=description,
                                            tags=tags, client=request.user)

                return CreateResponse()
            except Exception:
                return ErrorResponse(message="Category Does Not Exist!", status_code=status.HTTP_406_NOT_ACCEPTABLE)

        else:
            return ErrorResponse(message=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'attachment_file': {
                        'type': 'string',
                        'format': 'binary'
                    },
                    'task_id': {
                        'type': 'string'
                    },

                }
            }},
        tags=['Task'],
        responses={202: str},
    )
    def set_attachment_file(self, request: Request):
        serializer = TaskAttachmentFile(data=request.data)
        if serializer.is_valid():
            task_id = serializer.validated_data.get(TaskVO.task_id, None)
            task_attachment_file = serializer.validated_data.get(TaskVO.attachment_file, None)
            self.task_logic.update_task_attachments(task_id=task_id, filename=task_attachment_file)
            return UpdateResponse()

        else:
            return ErrorResponse(message=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[UpdateTaskSerializer],
        tags=['Task'],
        responses={202: str},
    )
    def patch(self, request: Request):
        serializer = UpdateTaskSerializer(data=request.query_params)
        if serializer.is_valid():
            task_id = serializer.validated_data.get('task_id')
            try:
                self.task_logic.make_task_done(task_id=task_id, user=request.user)

                return UpdateResponse()

            except Exception as e:

                return Response(data=str(e), status=status.HTTP_406_NOT_ACCEPTABLE)

        else:
            return ErrorResponse(message=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=['Task'],
        responses={200: GetTaskSerializer},
    )
    def get_tasks_related_to_user_skills(self, request: Request):
        tasks = self.task_logic.get_tasks_related_to_user_skills(user=request.user)
        serialized_response = GetTaskSerializer(tasks, many=True)
        return Response(serialized_response.data, status=status.HTTP_200_OK)


