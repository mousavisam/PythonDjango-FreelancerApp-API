from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema

from ....api.serializer.Contract.contract_serializer import ContractSerializer, GetContractSerializer, \
    UpdateContractSerializer
from ....logic.contract.contract_logic import ContractLogic
from ....shared.based_response.common_response import CreateResponse, ErrorResponse, UpdateResponse


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

    @extend_schema(
        parameters=[UpdateContractSerializer],
        tags=['Contract'],
        responses={202: None},
    )
    def patch(self, request: Request):
        serializer = UpdateContractSerializer(data=request.query_params)
        if serializer.is_valid():
            contract_id = serializer.validated_data.get("contract_id", None)
            contract_status = serializer.validated_data.get("status", None)
            try:
                self.contract_logic.update_contract_status(contract_id=contract_id, user=request.user,
                                                           status=contract_status)
                return UpdateResponse()

            except Exception as e:
                return Response(data=str(e), status=status.HTTP_406_NOT_ACCEPTABLE)

        else:
            return ErrorResponse(message=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)
