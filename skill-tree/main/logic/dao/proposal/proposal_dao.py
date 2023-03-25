from main.model.proposal_entity import Proposal


class ProposalDao:

    def create_proposal(self, **kwargs):
        Proposal.objects.create(**kwargs)