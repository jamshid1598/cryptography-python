from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField

User = get_user_model()

# Create your forms here.

class NewUserForm(UserCreationForm):
	phonenumber = PhoneNumberField(required=True)

	class Meta:
		model = User
		fields = ("username", "phonenumber", "password1", "password2")

	# def save(self, commit=True):
	# 	user = super(NewUserForm, self).save(commit=False)
	# 	user.phonenumber = self.cleaned_data['phonenumber']
	# 	if commit:
	# 		print('saved')
	# 		user.save()
	# 	print(commit)
	# 	return user