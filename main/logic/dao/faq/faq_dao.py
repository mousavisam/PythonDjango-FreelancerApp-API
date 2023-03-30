from django.db.models import QuerySet

from main.model.faq_entity import FAQ


class FAQDao:

    def get_faqs(self) -> QuerySet:

        return FAQ.objects.all()