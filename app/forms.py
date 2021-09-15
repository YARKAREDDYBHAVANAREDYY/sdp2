from django import forms
from .models import *
class Image(forms.ModelForm):
    class Meta:
        model = Fertilizer
        fields = "__all__"