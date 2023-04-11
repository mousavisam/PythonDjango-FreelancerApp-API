from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from main.api.serializer.invite.invite_serializer import SendInvitationSerializer
from main.logic.invite.invite_logic import InviteLogic
from main.shared.based_response.common_response import CreateResponse, ErrorResponse


class InviteController(ViewSet):

    def __init__(self):
        super().__init__()
        self.invite_logic = InviteLogic()

    @extend_schema(
        request=SendInvitationSerializer,
        tags=['invite'],
        responses={201: str},
    )
    def post(self, request: Request):

        serializer = SendInvitationSerializer(data=request.data)
        if serializer.is_valid():
            recipient_email = serializer.validated_data.get("recipient_email", None)
            try:
                self.invite_logic.send_invitation_email(recipient_email=recipient_email, user=request.user)

                return CreateResponse()

            except Exception as e:
                return Response(data=str(e), status=status.HTTP_404_NOT_FOUND)

        else:
            ErrorResponse(message=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)
