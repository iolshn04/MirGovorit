from django.contrib import admin

from cook.models import Product, Recipe, RecipeProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "times_cooked"
    list_display_links = ("pk",)


@admin.register(Recipe)
class PecipeAdmin(admin.ModelAdmin):
    list_display = "pk", "name"
    list_display_links = ("pk",)


@admin.register(RecipeProduct)
class RecipeProductAdmin(admin.ModelAdmin):
    list_display = "pk", "recipe", "product"
    list_display_links = ("pk",)