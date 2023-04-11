from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from main.api.serializer.user_session.user_session_serializer import UserSessionSerializer
from main.logic.report.report_logic import ReportLogic


class ReportController(ViewSet):

    def __init__(self):
        super().__init__()
        self.report_logic = ReportLogic()

    @extend_schema(
        tags=['report'],
        responses={200: str},
    )
    def get(self, request: Request):
        try:
            user_sessions, count_of_requested_tasks, count_of_served_tasks = \
                self.report_logic.generate_user_report(user=request.user)

            user_sessions_serialized = UserSessionSerializer(user_sessions, many=True)
            dict_of_response = {'user_logs': user_sessions_serialized.data,
                                'count_of_requested_tasks': count_of_requested_tasks,
                                'count_of_served_tasks': count_of_served_tasks}

            return Response(data=dict_of_response, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(data=str(e), status=status.HTTP_404_NOT_FOUND)

