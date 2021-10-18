from django import forms
from django.forms import ModelForm

from gram.models import Image

class PhotoForm(ModelForm):
    class Meta:
        model = Image
        fields = ('image','descriptions')