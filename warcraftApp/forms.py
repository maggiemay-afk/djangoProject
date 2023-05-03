from django import forms
from django.forms import ModelForm
from .models import SurveyModel


class SurveyForm(ModelForm):
    character_name = forms.TextInput()
    fav_zone = forms.TextInput()
    image_description = forms.TextInput()
    image = forms.ImageField()

    class Meta:
        model = SurveyModel
        fields = ['character_name', 'fav_zone', 'image_description', 'image']
        widgets = {
            'character_name' : TextInput(attrs={

            })
        }
