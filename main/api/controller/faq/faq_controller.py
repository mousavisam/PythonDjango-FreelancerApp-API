from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from main.api.serializer.FAQ.faq_serializer import GetFAQSerializer
from main.logic.faq.faq_logic import FAQLogic


class FAQController(ViewSet):

    permission_classes = [AllowAny]

    def __init__(self):
        super().__init__()
        self.faq_logic = FAQLogic()

    @extend_schema(
        tags=['FAQ'],
        responses={200: GetFAQSerializer},
    )
    def get(self, request: Request):
        faqs = self.faq_logic.get_faqs()
        serializer = GetFAQSerializer(faqs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
