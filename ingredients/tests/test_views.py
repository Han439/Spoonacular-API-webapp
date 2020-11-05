from django.test import TestCase, SimpleTestCase
from django.shortcuts import render, reverse

# Create your tests here.


class ViewTests(SimpleTestCase):

    def test_recipe_by_ingredients_view(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ingredients/search.html')
        self.assertIn('form', response.context)

    def test_all_recipes_view_with_valid_data(self):
        response = self.client.get(
            '/recipes/', data={'ingredients': 'banana, chocolate'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ingredients/recipes.html')
        self.assertIn('form', response.context)
        self.assertIn('recipes', response.context)

    def test_all_recipes_view_with_no_data(self):
        response = self.client.get('/recipes/')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('recipe_by_ingredients'))

    def test_recipe_by_ingredients_view(self):
        response = self.client.get('/recipes/1234/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ingredients/recipe_detail.html')
        self.assertIn('image', response.context)
        self.assertIn('steps', response.context)
        self.assertIn('info', response.context)
        self.assertIn('nutrition_widget', response.context)
