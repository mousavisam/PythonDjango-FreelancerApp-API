from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema

from main.api.serializer.Contract.contract_serializer import ContractSerializer, GetContractSerializer
from main.logic.contract.contract_logic import ContractLogic
from main.shared.based_response.common_response import CreateResponse, ErrorResponse


class ContractController(ViewSet):

    def __init__(self):
        super().__init__()
        self.contract_logic = ContractLogic()

    @extend_schema(
        request=ContractSerializer,
        tags=['Contract'],
        responses={201: str},
    )
    def post(self, request: Request):
        serializer = ContractSerializer(data=request.data)
        if serializer.is_valid():
            proposal = serializer.validated_data.get("proposal", None)
            delivery_time_in_day = serializer.validated_data.get("delivery_time_in_day", None)
            payment_amount = serializer.validated_data.get("payment_amount", None)
            payment_type = serializer.validated_data.get("payment_type", None)
            start_time = serializer.validated_data.get("start_time", None)
            try:
                self.contract_logic.create_contract(proposal_id=proposal.id, delivery_time_in_day=delivery_time_in_day,
                                                    payment_amount=payment_amount, payment_type=payment_type,
                                                    start_time=start_time, user=request.user)
                return CreateResponse()

            except Exception as e:
                return ErrorResponse(message=str(e), status_code=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return ErrorResponse(message=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=['Contract'],
        responses={200: GetContractSerializer},
    )
    def get(self, request: Request):
        user_contracts = self.contract_logic.get_user_contracts(user=request.user)
        serializer = GetContractSerializer(user_contracts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
