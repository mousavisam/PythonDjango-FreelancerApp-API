from django.urls import path

from ....api.controller.proposal.proposal_controller import ProposalController

urlpatterns = [
    path('create/', ProposalController.as_view({'post': 'post'}), name='create_proposal'),
    path('', ProposalController.as_view({'get': 'get'}), name='get_proposal'),
]