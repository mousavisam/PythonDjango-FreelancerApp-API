from datetime import timedelta
from typing import Union

from ..task.task_logic import TaskLogic
from ...enum.contract_status import ContractStatus
from ...enum.task_status import TaskStatus
from ...enum.user_status import UserType
from ...logic.dao.contract.contract_dao import ContractDao
from ...model.user_entity import User

from django.db.models import QuerySet


class ContractLogic:

    def __init__(self):
        super().__init__()
        self.dao = ContractDao()
        self.task_logic = TaskLogic()

    def create_contract(self, **kwargs):
        if kwargs.get("user").type == UserType.CLIENT:
            kwargs['end_time'] = kwargs.get("start_time") + timedelta(days=kwargs.get("delivery_time_in_day"))
            kwargs['status'] = ContractStatus.PENDING
            kwargs.pop('user')
            self.dao.create_contract(**kwargs)
        else:
            raise ValueError("Only Clients can create contracts")

    def get_user_contracts(self, user: User) -> Union[QuerySet, list]:
        return self.dao.get_user_contracts(user)

    def update_contract_status(self, contract_id, user, status):
        if user.type == UserType.FREELANCER:
            contract = self.dao.update_contract_status(contract_id=contract_id, status=status)
            if status == ContractStatus.APPROVED:
                self.task_logic.update_task_status(task=contract.proposal.task, task_status=TaskStatus.IN_PROGRESS)

        else:
            raise ValueError("Only Freelancers Can Update Contracts")
