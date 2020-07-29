from django import forms

class ByIngredients(forms.Form):
	ingredients = forms.CharField(max_length=200, help_text='What Ingredients Do You Have? (seperate by space)')