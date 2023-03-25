from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema

from main.api.serializer.proposal.proposal_serializer import CreateProposalSerializer
from main.logic.proposal.proposal_logic import ProposalLogic
from main.shared.based_response.common_response import CreateResponse, ErrorResponse


class ProposalController(ViewSet):

    def __init__(self):
        super().__init__()
        self.proposal_logic = ProposalLogic()

    @extend_schema(
        request=CreateProposalSerializer,
        tags=['proposal'],
        responses={201: str},
    )
    def post(self, request: Request):

        serializer = CreateProposalSerializer(data=request.data)
        if serializer.is_valid():
            delivery_time_in_day = serializer.validated_data.get("delivery_time_in_day", None)
            payment_amount = serializer.validated_data.get("payment_amount", None)
            description = serializer.validated_data.get("description", None)
            task_id = serializer.validated_data.get("task_id")
            try:
                self.proposal_logic.create_proposal(delivery_time_in_day=delivery_time_in_day,
                                                    payment_amount=payment_amount,
                                                    description=description, task_id=task_id, freelancer=request.user)

                return CreateResponse()

            except Exception as e:
                return Response(data=str(e), status=status.HTTP_404_NOT_FOUND)

        else:
            ErrorResponse(message=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)
