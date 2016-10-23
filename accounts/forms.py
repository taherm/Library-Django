from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
	'''
	Extension to UserCreationForm, add three fields:
	first_name, last_name and email.
	'''

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email")