from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .. import views


# Create your tests here.


class TestUrlsNameResolve(SimpleTestCase):

    def test_index_url_resolve(self):
        url = reverse('recipe_by_ingredients')
        self.assertEqual(resolve(url).func, views.recipe_by_ingredients)

    def test_index_url_resolve(self):
        url = reverse('all_recipes')
        self.assertEqual(resolve(url).func, views.all_recipes)

    def test_index_url_resolve(self):
        url = reverse('recipe_detail', kwargs={'recipe_id': 1898})
        self.assertEqual(resolve(url).func, views.recipe_detail)
