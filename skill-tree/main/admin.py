from django.contrib import admin

from .model.category_entity import Category
from .model.user_entity import User


admin.site.register(User)
admin.site.register(Category)

