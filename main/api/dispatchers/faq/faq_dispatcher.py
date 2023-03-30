from django.urls import path

from main.api.controller.faq.faq_controller import FAQController

urlpatterns = [
    path('', FAQController.as_view({'get': 'get'}), name='get_faqs'),
]
