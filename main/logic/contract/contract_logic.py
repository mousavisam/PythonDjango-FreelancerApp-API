from datetime import timedelta
from typing import Union

from ..task.task_logic import TaskLogic
from ...enum.contract_status import ContractStatus
from ...enum.task_status import TaskStatus
from ...enum.user_status import UserType
from ...logic.dao.contract.contract_dao import ContractDao
from ...model.contract_entity import Contract
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
        contract = self.get_contract_by_id(contract_id=contract_id)
        if user.type == UserType.FREELANCER and user == contract.proposal.freelancer:
            contract = self.dao.update_contract_status(contract_id=contract_id, status=status)
            if status == ContractStatus.APPROVED:
                self.task_logic.set_freelancer_for_task(user=contract.proposal.freelancer, task=contract.proposal.task)
                self.task_logic.update_task_status(task=contract.proposal.task, task_status=TaskStatus.IN_PROGRESS)

        else:
            raise ValueError("Only Freelancers Can Update Contracts")

    def get_contract_by_id(self, contract_id: int) -> Contract:
        return self.dao.get_contract_by_id(contract_id=contract_id)

    def make_contract_done(self, is_done: bool, contract_id: int, user: User, client_message: str = None) -> None:
        contract = self.get_contract_by_id(contract_id=contract_id)
        if contract.proposal.task.client == user:
            return self.dao.make_contract_done(is_done=is_done, contract=contract, client_message=client_message)
        else:
            raise ValueError("This user is not the client contract")
