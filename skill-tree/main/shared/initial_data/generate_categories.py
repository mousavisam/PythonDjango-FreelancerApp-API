from main.logic.category.category_logic import CategoryLogic
from main.model.category_entity import Category
from main.shared.initial_data.category_dict import CategoryDict


class GenerateCategories:

    def __init__(self):
        super().__init__()

    def add_new_categories(self):
        for key, value in CategoryDict.items():
            main_category = Category.objects.get_or_create(title=key)
            for sub_category in value:
                Category.objects.get_or_create(parent=main_category[0], title=sub_category['title'])
