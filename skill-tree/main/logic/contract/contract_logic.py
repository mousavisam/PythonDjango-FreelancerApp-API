from datetime import timedelta
from typing import Union

from main.enum.contract_status import ContractStatus
from main.enum.user_status import UserType
from main.logic.dao.contract.contract_dao import ContractDao
from main.model.user_entity import User

from django.db.models import QuerySet


class ContractLogic:

    def __init__(self):
        super().__init__()
        self.dao = ContractDao()

    def create_contract(self, **kwargs):
        if kwargs.get("user") == UserType.CLIENT:
            kwargs['end_time'] = kwargs.get("start_time") + timedelta(days=kwargs.get("delivery_time_in_day"))
            kwargs['status'] = ContractStatus.PENDING
            self.dao.create_contract(**kwargs)
        else:
            raise ValueError("Only Clients can create contracts")

    def get_user_contracts(self, user: User) -> Union[QuerySet, list]:
        return self.dao.get_user_contracts(user)
