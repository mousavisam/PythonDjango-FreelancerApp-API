from django.urls import path

from main.api.controller.browse.browse_controller import BrowseController

urlpatterns = [
    path('', BrowseController.as_view({'get': 'search'}), name='search'),
]