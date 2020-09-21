from django.test import TestCase, SimpleTestCase
from django.shortcuts import render, reverse

# Create your tests here.
class ViewTests(SimpleTestCase):

	def test_recipe_by_ingredients_view(self):
		response = self.client.get('/')

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'ingredients/search.html')
		self.assertTrue('form' in response.context)

	def test_all_recipes_view(self):
		response = self.client.get('/recipes/', data={'ingredients': 'banana, chocolate'})

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'ingredients/recipes.html')
		self.assertTrue('form' in response.context)
		self.assertTrue('recipes' in response.context)

	def test_all_recipes_view_with_no_data(self):
		response = self.client.get('/recipes/')

		self.assertRedirects(response, reverse('recipe_by_ingredients'))

	def test_recipe_by_ingredients_view(self):
		response = self.client.get('/recipes/1234/')

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'ingredients/recipe_detail.html')
		self.assertTrue('image' in response.context)
		self.assertTrue('steps' in response.context)
		self.assertTrue('info' in response.context)
		self.assertTrue('nutrition_widget' in response.context)