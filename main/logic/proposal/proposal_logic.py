from typing import Union
from django.db.models import QuerySet

from ...enum.task_status import TaskStatus
from ...enum.user_status import UserType
from ...logic.dao.proposal.proposal_dao import ProposalDao
from ...logic.task.task_logic import TaskLogic
from django.core.exceptions import ObjectDoesNotExist
from ...model.user_entity import User
from ...enum.proposal_status import ProposalStatus


class ProposalLogic:
    def __init__(self):
        super().__init__()
        self.task_logic = TaskLogic()
        self.dao = ProposalDao()

    def create_proposal(self, **kwargs):
        if kwargs['freelancer'].type == UserType.FREELANCER:
            task = self.task_logic.get_task_by_id(task_id=kwargs['task_id'])
            if task and task.status == TaskStatus.UNASSIGNED:
                kwargs['task_id'] = task.id
                self.dao.create_proposal(**kwargs)

            else:
                raise ObjectDoesNotExist

        else:
            raise ValueError("User must be Freelancer")

    def get_user_proposals(self, user: User) -> Union[QuerySet, list]:
        return self.dao.get_user_proposals(user)

    def update_proposal_status(self, proposal_id: int, status: ProposalStatus, user: User) -> None:
        if user.type == UserType.CLIENT:
            self.dao.update_proposal_status(proposal_id=proposal_id, status=status)

        else:
            raise ValueError("Freelancers cannot update proposals")
