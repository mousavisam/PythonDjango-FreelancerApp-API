from main.model.faq_entity import FAQ
from main.shared.initial_data.faq.faq_dict import FAQDict


class GenerateFAQ:

    def insert_faq(self):
        for key, value in FAQDict.items():
            FAQ.objects.create(question=key, answer=value)