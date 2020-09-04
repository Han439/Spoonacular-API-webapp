from django import forms

class ByIngredients(forms.Form):
	ingredients = forms.CharField(max_length=200)