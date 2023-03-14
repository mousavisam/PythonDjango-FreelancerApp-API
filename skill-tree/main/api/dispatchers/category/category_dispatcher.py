from django.urls import path

from main.api.controller.category.category_controller import CategoryController

urlpatterns = [
    path('search/', CategoryController.as_view({'get': 'search'}), name='search'),
]
