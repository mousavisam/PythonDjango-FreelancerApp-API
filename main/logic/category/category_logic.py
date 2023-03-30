from typing import Tuple

from django.db.models import QuerySet

from ...logic.dao.category.category_dao import CategoryDao
from ...model.category_entity import Category
from ...model.vo.category.category_vo import CategoryVO


class CategoryLogic:
    def __init__(self):
        self.dao = CategoryDao()

    def search_category_by_title(self, title: str):

        category, sub_categories = self.dao.search_category_by_title(title=title)
        if sub_categories:
            response = dict()
            response[category.title] = list()
            for item in sub_categories:
                response[category.title].append({CategoryVO.title: item.title, CategoryVO.description: item.description})
                return response
        return category

    def get_category_by_title(self, title: str) -> Category:
        return self.dao.get_category_by_title(title)

    def get_all_categories(self) -> QuerySet:
        return self.dao.get_all_categories()
