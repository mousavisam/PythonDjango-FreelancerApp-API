from typing import Union
from django.db.models import QuerySet
from ....model.proposal_entity import Proposal
from ....model.user_entity import User
from ....enum.user_status import UserType
from ....enum.proposal_status import ProposalStatus


class ProposalDao:

    def create_proposal(self, **kwargs):
        Proposal.objects.create(**kwargs)

    def get_user_proposals(self, user: User) -> Union[QuerySet, list]:
        if user.type == UserType.FREELANCER:
            return Proposal.objects.filter(freelancer=user)

        elif user.type == UserType.CLIENT:
            return Proposal.objects.filter(task__client=user)

        else:
            return list()

    def update_proposal_status(self, proposal_id: int, status: ProposalStatus) -> None:
        proposal = Proposal.objects.filter(id=proposal_id).first()
        proposal.status = status
        proposal.save()
