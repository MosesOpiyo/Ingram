from django import forms
from django.forms import ModelForm

from gram.models import Picture

class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = '__all__'
        exclude = ('likes','post_date')