from django.urls import path
from .views import add_product_to_recipe, cook_recipe, show_recipes_without_product

app_name = "cook"

urlpatterns = [
    path('add_product_to_recipe/', add_product_to_recipe, name='add-product'),
    path('cook_recipe/', cook_recipe, name='cook-recipe'),
    path('show_recipes_without_product/', show_recipes_without_product, name='recipes-without-product'),
]