from django.urls import path

from main.api.controller.invite.invite_controller import InviteController

urlpatterns = [
    path('', InviteController.as_view({'post': 'post'}), name='send_invitation'),
]