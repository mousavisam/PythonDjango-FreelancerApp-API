from django.urls import path, include

urlpatterns = [
    path('auth/', include('main.api.dispatcher.authentication.authentication_dispatcher')),

]