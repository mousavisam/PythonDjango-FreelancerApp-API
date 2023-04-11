from django.urls import path

from ...controller.registration.login_controller import LoginController
from ...controller.registration.logout_controller import LogoutController
from ....api.controller.registration.register_controller import RegisterController

urlpatterns = [
    path('register/', RegisterController.as_view({'get': 'retrieve'}), name='register'),
    path('register/create/', RegisterController.as_view({'post': 'post'}), name='create_register'),
    path('login/', LoginController.as_view({'post': 'post'}), name='login'),
    path('signin/', RegisterController.as_view({'post': 'google_signin'}), name='signin'),
    path('login/update_user_type', LoginController.as_view({'patch':'update_user_type'}), name='update_user_type'),
    path('login/get_user', LoginController.as_view({'get':'get_user'}), name='get_user'),
    path('logout/', LogoutController.as_view({'post': 'post'}), name='logout')
]
