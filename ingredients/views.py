from django.shortcuts import render, reverse, redirect
from .forms import ByIngredients
import dotenv, os, requests
from dotenv import load_dotenv
import random


load_dotenv()

keys = os.getenv('SPOONACULAR_API_KEY')

# Create your views here.
def recipe_by_ingredients(request):
	form = ByIngredients()
	context = {'form': form}
	return render(request, 'ingredients/search.html', {'form': form})

def all_recipes(request):
	form = ByIngredients(request.GET)
	if form.is_valid():
		ingredients = str(form.cleaned_data['ingredients'])
		# access Spoonacular API endpoint for recipes.
		if ingredients.strip() != '':
			ingredients_list = str(form.cleaned_data['ingredients']).split()
			# config API before sending
			uri = 'https://api.spoonacular.com/recipes/findByIngredients'
			params = {'apiKey': keys, 'ingredients': ingredients_list, 'number': '50'}
			
			# get the API response
			response = requests.get(uri, params=params)
			recipes = response.json()
			random.shuffle(recipes)
		else:
			recipes = []

	# pack up datas send for templates render
		context = {
				'recipes': recipes[:8],
				'form': form,
				}
		return render(request, 'ingredients/recipes.html', context)
	else:
		return redirect(reverse('recipe_by_ingredients'))

def recipe_detail(request, recipe_id):

	# recipe steps
	recipe_detail_endpoint = f'https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions'
	
	params = {'apiKey': keys, "defaultCss":"true"}

	response = requests.get(recipe_detail_endpoint, params={'apiKey': keys})
	recipe_step = response.json()
	if recipe_step != []:
		steps = recipe_step[0]['steps']
	else:
		steps = ['There is no recipe yet!']

	# recipe ingredients
	info_endpoint = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
	info = requests.get(info_endpoint, params={'apiKey': keys}).json()

	# get Ingredients Price Break Down Widget
	widget_header = {'accept': 'text/html'}

	# get Nutrition Break Down Widget
	nutrition_endpoint = f'https://api.spoonacular.com/recipes/{recipe_id}/nutritionWidget'
	nutrition_widget = requests.get(nutrition_endpoint, params=params, headers=widget_header).text

	context = {
		'image': f'https://spoonacular.com/recipeImages/{recipe_id}-556x370.jpg',
		'steps': steps,
		'info' : info,
		'nutrition_widget': nutrition_widget
	}

	return render(request, 'ingredients/recipe_detail.html', context)