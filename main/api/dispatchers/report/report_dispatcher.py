from django.urls import path

from main.api.controller.report.report_controller import ReportController

urlpatterns = [
    path('', ReportController.as_view({'get': 'get'}), name='report')
]