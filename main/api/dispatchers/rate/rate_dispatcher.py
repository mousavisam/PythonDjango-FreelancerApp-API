from django.urls import path

from main.api.controller.rate.rate_controller import RateController

urlpatterns = [
    path('', RateController.as_view({'post': 'post'}), name='create_rate'),
]
