from django.urls import path

from .views import recipe_by_ingredients, all_recipes, recipe_detail

urlpatterns = [
	path('', recipe_by_ingredients, name='recipe_by_ingredients'),
	path('recipes/', all_recipes, name='all_recipes'),
	path('recipes/<int:recipe_id>/', recipe_detail, name='recipe_detail')
]