from django import forms
from .models import Image, Imagemain


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"
class ImageForm1(forms.ModelForm):
    class Meta:
        model = Imagemain
        fields = "__all__"
