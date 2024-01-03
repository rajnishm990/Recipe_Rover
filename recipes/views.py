from django.views.generic import (
    CreateView, ListView, 
    DetailView ,DeleteView ,
    UpdateView
    )
from .models import Recipe
from .forms import RecipeForm
from django.db.models import Q

from django.contrib.auth.mixins import (
    LoginRequiredMixin , UserPassesTestMixin
    )


class Recipes(ListView):
    template_name = "recipes/recipes.html"
    model = Recipe
    context_object_name = "recipes"

    def get_queryset(self ,**kwargs):
        query = self.request.GET.get('q')
        if query:
            recipes = self.model.objects.filter(
                Q(title__icontains=query)|
                Q(description__icontains=query)|
                Q(ingredients__icontains=query)|
                Q(instructions__icontains=query)
            )
        else:
            recipes = self.model.objects.all()
        
        return recipes


class AddRecipe(LoginRequiredMixin, CreateView):
    template_name = "recipes/add_recipe.html"
    model = Recipe
    success_url = "/recipes/"
    form_class = RecipeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)


class RecipeDetail(DetailView):
    template_name = "recipes/recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"
 
class EditRecipe(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    template_name = 'recipes/edit_recipe.html'
    model=Recipe
    form_class = RecipeForm
    success_url ="/recipes/"
    
    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteRecipe(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    
    model = Recipe
    success_url ="/recipes/"

    def test_func(self):
        return self.request.user == self.get_object().user
