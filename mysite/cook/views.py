from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Recipe, RecipeProduct


def add_product_to_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')

        recipe = get_object_or_404(Recipe, id=recipe_id)
        product = get_object_or_404(Product, id=product_id)

        recipe_product, _ = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
        recipe_product.weight = weight
        recipe_product.save()

        return HttpResponse('Product added to recipe successfully.')


def cook_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')

        recipe = get_object_or_404(Recipe, id=recipe_id)
        recipe_products = recipe.recipeproduct_set.all()

        for recipe_product in recipe_products:
            product = recipe_product.product
            product.times_cooked += 1
            product.save()

        return HttpResponse('Recipe cooked successfully.')


def show_recipes_without_product(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        product = get_object_or_404(Product, id=product_id)

        recipes_without_product = Recipe.objects.exclude(recipeproduct__product=product)\
            .exclude(recipeproduct__weight__gte=10)

        return render(request, 'cook/recipes_without_product.html', {'recipes': recipes_without_product})