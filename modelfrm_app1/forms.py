from django import forms

from .models import userreg


class RegistrationForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = userreg
		fields = "__all__"


