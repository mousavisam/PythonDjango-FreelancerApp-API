from rest_framework.viewsets import ViewSet
from rest_framework.request import Request

from main.shared.based_response.common_response import CreateResponse


class TaskController(ViewSet):

    def __init__(self):
        super().__init__()
        self.task_logic = TaskLogic()


    def post(self, request: Request):

        serializer = CreateTaskSerializer(data=request.data)
        if serializer.is_valid:

            return CreateResponse()
