from rest_framework import serializers

from main.model.category_entity import Category


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)


class CategoryResponseSerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()

    class Meta:
        model = Category

        fields = ['parent', 'title', 'description']

    def get_parent(self, obj):
        return obj.parent.title

