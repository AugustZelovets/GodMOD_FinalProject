import requests
from django import forms
from django.forms import inlineformset_factory, ModelForm

from .models import *


class ModVersionInline(forms.ModelForm):
    class Meta:
        model = ModVersion
        fields = '__all__'


class ModVersionCreationForm(forms.ModelForm):

    class Meta:
        model = ModVersion
        fields = '__all__'


class ModCreationForm(forms.ModelForm):
    class Meta:
        model = Mod
        exclude = 'author',





ModInlineFormSet = inlineformset_factory(Mod, ModVersion,
                                         form=ModVersionInline,
                                         extra=1,
                                         can_delete=False,
                                         fields='__all__')


# class RecipeForm(ModelForm):
#     error_css_class = 'error-field'
#     required_css_class = 'required-field'
#     #name = forms.CharField(help_text='This is your help! <a href="/contact">Contact us</a>')
#
#     # descriptions = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
#     class Meta:
#         model = Mod
#         fields = ['name', 'description', 'directions']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # django-crispy-forms
#         for field in self.fields:
#             new_data = {
#                 "placeholder": f'Recipe {str(field)}',
#                 "class": 'form-control',
#                 # "hx-post": ".",
#                 # "hx-trigger": "keyup changed delay:500ms",
#                 # "hx-target": "#recipe-container",
#                 # "hx-swap": "outerHTML"
#             }
#             self.fields[str(field)].widget.attrs.update(
#                 new_data
#             )
#         # self.fields['name'].label = ''
#         # self.fields['name'].widget.attrs.update({'class': 'form-control-2'})
#         self.fields['description'].widget.attrs.update({'rows': '2'})
#         self.fields['directions'].widget.attrs.update({'rows': '4'})


# class RecipeIngredientForm(ModelForm):
#     class Meta:
#         model = ModVersion
#         fields = ['name', 'quantity', 'unit']