from django.urls import path

from main.api.controller.profile.profile_controller import ProfileController

urlpatterns = [
    path('update/', ProfileController.as_view({'patch': 'patch'}), name='update_profile'),
    path('update_image/', ProfileController.as_view({'patch': 'set_profile_image'}), name='update_profile_image'),
    path('', ProfileController.as_view({'get': 'get'}), name='get_profile'),

]