from typing import Tuple

from django.core.exceptions import ObjectDoesNotExist
from main.model.category_entity import Category


class CategoryDao:

    def search_category_by_title(self, title: str) -> Tuple:
        category = Category.objects.filter(title__contains=title).first()
        if category:
            if not category.parent:
                sub_categories = Category.objects.filter(parent=category.id)

                return category, sub_categories

            return category, None
        else:
            raise ValueError("Object Does Not Exist")

    def get_category_by_title(self, title: str) -> Category:
        return Category.objects.filter(title__contains=title).first()
