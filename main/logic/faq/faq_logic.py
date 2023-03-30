from django.db.models import QuerySet

from main.logic.dao.faq.faq_dao import FAQDao


class FAQLogic:

    def __init__(self):
        super().__init__()
        self.dao = FAQDao()

    def get_faqs(self) -> QuerySet:
        return self.dao.get_faqs()
