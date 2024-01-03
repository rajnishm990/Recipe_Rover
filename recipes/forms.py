from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "ingredients",
            "instructions",
            "image",
            "image_alt",
        ]

        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())

        widgets = {"description": forms.Textarea(attrs={"rows": 5})}

        labels = {
            "title": "Recipe Title",
            "description": "Description",
            "ingredients": "Recipe Ingredients",
            "instructions": "Recipe Instructions",
            "image": "Recipe Image",
            "image_alt": "Description of Image",
        }
