from django import forms
from django.contrib import messages
# from django.contrib import messages
import phonenumbers

class GenerateKeyForm(forms.Form):
	name = forms.CharField(max_length=100, 
                           widget=forms.TextInput(attrs={
                               'type':"text", 
                               'class':"form-control mt-2", 
                               'placeholder':"Enter key name ..."}))
	
	def clean_name(self):
		name = self.cleaned_data.get('name')
		if not name:
			raise forms.ValidationError("This field must be filled!")
		return name