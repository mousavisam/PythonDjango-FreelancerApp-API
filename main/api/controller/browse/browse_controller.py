from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from main.api.serializer.Browse.browse_serializer import BrowseSerializer
from main.api.serializer.Registration.register_serializer import SearchUserSerializer
from main.api.serializer.Task.task_serializer import SearchTaskSerializer
from main.logic.search.search_logic import SearchLogic
from main.shared.based_response.common_response import ErrorResponse


class BrowseController(ViewSet):

    def __init__(self):
        super().__init__()
        self.search_logic = SearchLogic()

    @extend_schema(
        parameters=[BrowseSerializer],
        tags=['Search'],
        responses={200: list},
    )
    def search(self, request: Request):

        serializer = BrowseSerializer(data=request.query_params)
        if serializer.is_valid():
            keyword = serializer.validated_data.get("keyword")
            users, tasks = self.search_logic.search_by_keyword(keyword=keyword)
            user_serializer = SearchUserSerializer(users, many=True)
            task_serializer = SearchTaskSerializer(tasks, many=True)
            response = {'users': user_serializer.data, 'tasks': task_serializer.data}
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return ErrorResponse(message=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)
