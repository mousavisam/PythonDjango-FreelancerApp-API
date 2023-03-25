from django.urls import path

from main.api.controller.proposal.proposal_controller import ProposalController

urlpatterns = [
    path('create/', ProposalController.as_view({'post': 'post'}), name='create_proposal'),
]