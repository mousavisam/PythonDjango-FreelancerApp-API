from django.urls import path

from ....api.controller.Contract.contract_controller import ContractController

urlpatterns = [
    path('', ContractController.as_view({'post': 'post'}), name='create_contract'),
    path('', ContractController.as_view({'get': 'get'}), name='get_contract'),
    path('', ContractController.as_view({'patch': 'patch'}), name='update_contract'),
    path('make_contract_done', ContractController.as_view({'patch': 'make_contract_done'}), name='make_contract_done'),
]
