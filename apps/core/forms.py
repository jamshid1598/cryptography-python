from django import forms
from django.contrib import messages
# from django.contrib import messages
import phonenumbers

class GenerateKeyForm(forms.Form):
	name = forms.CharField(max_length=200, 
                           widget=forms.TextInput(attrs={
                               'type': "text", 'name': 'name', 'id': 'name', 
                               'placeholder': "Key name ..."}))
	
	def clean_name(self):
		name = self.cleaned_data.get('name')
		if not name:
			raise forms.ValidationError("This field must be filled!")
		return name


class encryptDecryptForm(forms.Form):
	private_key = forms.CharField(widget=forms.Textarea(attrs={
                               'type':"text", 'name': "private_key", 'id': 'private_key', 
                               'cols':70, 'rows':8,'placeholder':"Enter private key ..."}), required=False)
	public_key = forms.CharField(widget=forms.Textarea(attrs={
                               'type':"text", 'name': "public_key", 'id': 'public_key', 
                               'cols':70, 'rows':8,'placeholder':"Enter public key ..."}), required=False)
	message = forms.CharField(widget=forms.Textarea(attrs={
                               'type':"text", 'name': "result_text", 'id': "result_text", 
                               'cols': 70, 'rows': 20,
                               'placeholder': "Please enter what needs to be encrypted or decrypted ..."}), required=True)
	
	def clean(self):
		private_key = self.cleaned_data.get('private_key')
		public_key = self.cleaned_data.get('public_key')
		if not (private_key or public_key):
			raise forms.ValidationError("Private key or public key must be filled")

	def clean_message(self):
		message = self.cleaned_data.get('message')
		if not message:
			raise forms.ValidationError("This field must be filled with some text!")
		return message