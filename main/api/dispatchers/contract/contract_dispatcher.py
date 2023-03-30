from django.urls import path

from ....api.controller.Contract.contract_controller import ContractController

urlpatterns = [
    path('', ContractController.as_view({'post': 'post'}), name='create_contract'),
    path('', ContractController.as_view({'get': 'get'}), name='get_contract'),
    path('', ContractController.as_view({'patch': 'patch'}), name='update_contract'),
]
