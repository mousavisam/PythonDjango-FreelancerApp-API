from typing import Tuple

from django.db.models import QuerySet

from main.model.category_entity import Category


class CategoryDao:

    def search_category_by_title(self, title: str) -> Tuple:
        category = Category.objects.filter(title__contains=title).first()
        if not category.parent:
            sub_categories = Category.objects.filter(parent=category.id)

            return category, sub_categories

        return category
