from main.enum.user_status import UserType
from main.logic.dao.proposal.proposal_dao import ProposalDao
from main.logic.task.task_logic import TaskLogic
from django.core.exceptions import ObjectDoesNotExist


class ProposalLogic:
    def __init__(self):
        super().__init__()
        self.task_logic = TaskLogic()
        self.dao = ProposalDao()

    def create_proposal(self, **kwargs):
        if kwargs['freelancer'].type == UserType.FREELANCER:
            task = self.task_logic.get_task_by_id(task_id=kwargs['task_id'])
            if task:
                kwargs['task_id'] = task.id
                self.dao.create_proposal(**kwargs)


            else:
                raise ObjectDoesNotExist

        else:
            raise ValueError("User must be Freelancer")
