from typing import Tuple

from django.db.models import QuerySet

from main.logic.dao.category.category_dao import CategoryDao
from main.model.vo.category.category_vo import CategoryVO


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
