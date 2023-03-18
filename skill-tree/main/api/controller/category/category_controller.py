from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from main.api.serializer.Category.category_serializer import CategorySerializer, CategoryResponseSerializer
from main.logic.category.category_logic import CategoryLogic
from main.model.category_entity import Category
from main.model.vo.category.category_vo import CategoryVO

from drf_spectacular.utils import extend_schema


class CategoryController(ViewSet):

    def __init__(self):
        super().__init__()
        self.category_logic = CategoryLogic()

    @extend_schema(
        parameters=[CategorySerializer],
        tags=[CategoryVO.category],
        responses={201: dict},
    )
    def search(self, request: Request):
        serializer = CategorySerializer(data=request.query_params)
        if serializer.is_valid():
            title = serializer.validated_data.get(CategoryVO.title, None)
            response = self.category_logic.search_category_by_title(title)
            if isinstance(response, Category):
                serialized_response = CategoryResponseSerializer(response)
                return Response(serialized_response.data, status=status.HTTP_200_OK)

            else:
                return Response(data=response, status=status.HTTP_200_OK)
