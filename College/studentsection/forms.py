from django import forms
from django.contrib.auth.models import User

from .models import Profile


class Userupdateform(forms.ModelForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username','email']

		

class ProfileUpdateform(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['image']