from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.serializers import UserSerializer

from .models import Ingredient, Recipe, Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug',)


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit',)


class RecipeSerializer(ModelSerializer):
    tags = TagSerializer(many=True)
    author = UserSerializer()
    ingredients = IngredientSerializer(many=True)
    is_favorited = SerializerMethodField(
        method_name='get_is_favorite',
    )
    is_in_shopping_cart = SerializerMethodField(
        method_name='get_is_in_shopping_cart',
    )

    class Meta:
        model = Recipe
        fields = (
            'id', 'tags', 'author', 'ingredients', 'is_favorited',
            'is_in_shopping_cart',
        )

    def get_is_favorite(self, obj):
        return len(
            self.context['request'].user.favorites.filter(recipe=obj)
        ) == 1

    def get_is_in_shopping_cart(self, obj):
        return len(
            self.context['request'].user.shopping_cart
                .filter(recipes__in=[obj])
        ) == 1