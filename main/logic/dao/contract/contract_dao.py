from typing import Union
from django.db.models import QuerySet

from main.enum.contract_status import ContractStatus
from main.enum.user_status import UserType
from main.model.contract_entity import Contract
from main.model.user_entity import User


class ContractDao:

    def create_contract(self, **kwargs) -> None:
        Contract.objects.create(**kwargs)

    def get_contract_by_id(self, contract_id: int) -> Contract:
        return Contract.objects.filter(id=contract_id).first()

    def get_user_contracts(self, user: User) -> Union[QuerySet, list]:
        if user.type == UserType.CLIENT:
            return Contract.objects.filter(proposal__task__client=user).order_by('-creation_time')
        elif user.type == UserType.FREELANCER:
            return Contract.objects.filter(proposal__freelancer=user).order_by('-creation_time')
        else:
            return list()

    def update_contract_status(self, contract_id: int, status: ContractStatus) -> Contract:
        contract = Contract.objects.filter(id=contract_id).first()
        contract.status = status
        contract.save()
        return contract

    def make_contract_done(self, contract: Contract, client_message, is_done) -> None:
        contract.is_done = is_done
        contract.client_message = client_message
        contract.save()
