from django.urls import path

from ...controller.authentication.login_controller import LoginController
from ...controller.authentication.sign_up_controller import SignUpController

urlpatterns = [
    path('signup/', SignUpController.as_view({'get': 'retrieve'}), name='sign_up'),
    path('signup/create/', SignUpController.as_view({'post': 'post'}), name='create_sign_up'),
    path('login/', LoginController.as_view({'post': 'post'}), name='login'),
]