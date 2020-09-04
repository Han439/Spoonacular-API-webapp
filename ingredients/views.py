from django.shortcuts import render
from .forms import ByIngredients
import dotenv, os, requests
from dotenv import load_dotenv


load_dotenv()

keys = os.getenv('SPOONACULAR_API_KEY')

# Create your views here.
def recipe_by_ingredients(request):
	form = ByIngredients()
	context = {'form': form}
	return render(request, 'ingredients\\search.html', {'form': form})

def all_recipes(request):
	form = ByIngredients(request.GET)
	if form.is_valid():
		ingredients = str(form.cleaned_data['ingredients'])
		# access Spoonacular API endpoint for recipes.
		if ingredients.strip() != '':
			ingredients_list = str(form.cleaned_data['ingredients']).split()
			# config API before sending
			uri = 'https://api.spoonacular.com/recipes/findByIngredients'
			params = {'apiKey': keys, 'ingredients': ingredients_list, 'number': '5'}
			
			# get the API response
			response = requests.get(uri, params=params)
			recipes = response.json()

			# get link to to recipe
				
			# recipe_param = {'apiKey': keys}

			# for recipe_num in range(len(recipes)):
			# 	recipe_id = recipes[recipe_num]['id']
			# 	url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
			# 	res = requests.get(url, params=recipe_param).json()
			# 	if 'spoonacularSourceUrl' in res.keys():
			# 		sourceUrl = res['spoonacularSourceUrl']
			# 	else:
			# 		sourceUrl = res['sourceUrl']

			# 	recipes[recipe_num]['sourceUrl'] = sourceUrl
		else:
			recipes = []

	# pack up datas send for templates render
	context = {
			'recipes': recipes,
			'form': form,
			}

	return render(request, 'ingredients/recipes.html', context)

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

	# price_json_endpoint = f'https://api.spoonacular.com/recipes/{recipe_id}/priceBreakdownWidget.json'
	# price_json = requests.get(price_json_endpoint, params={'apiKey': keys}).json()

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