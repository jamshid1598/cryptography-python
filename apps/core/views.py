from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import (
	CreateView, 
	UpdateView,
)

# CRYPTOGRAPHY
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# local files
from .models import (
	CryptoKey,
	CryptoMessage,
)
from .forms import (
	GenerateKeyForm,
	encryptDecryptForm,
)
from .utils import (
    get_generated_key,
	encryption_view,
	decryption_view,
)

def get_queryset(id=None):
	try:
		return CryptoKey.objects.get(id=id), CryptoKey.objects.all()
	except:
		return None, CryptoKey.objects.all()


def home_view(request, id=None, *args, **kwargs):
	context = {}
	template_name = 'crytokey.html'
	context['key_info'], context['key_queryset'] = get_queryset(id)    
	return render(request, template_name, context)


def generate_key_view(request, *args, **kwargs):
	form = GenerateKeyForm(request.POST)
	if form.is_valid():
		name = form.cleaned_data.get('name')
		private_key, public_key = get_generated_key(request, *args, **kwargs)
		key_instance = CryptoKey.objects.create(name=name, private_key=private_key, public_key=public_key)
		return redirect("core:home", id=key_instance.id)
	else:
		form = GenerateKeyForm()
		return redirect("core:home")


def encryptDecryptView(request, *args, **kwargs):
	context = {}
	form = encryptDecryptForm(request.POST)
	if form.is_valid():
		private_key = form.cleaned_data.get('private_key')
		public_key = form.cleaned_data.get('public_key')
		message = form.cleaned_data.get('')
	context['form'] = form
	return render(request, 'message.html', context)


class EncryptDecryptView(View):
	template_name='message.html'
	context={}
	
	def get(self, request, *args, **kwargs):
		form = encryptDecryptForm()
		self.context['form'] = form
		return render(request, self.template_name, self.context)
 
	def post(self, request, *args, **kwargs):
		form = encryptDecryptForm(request.POST)
		if form.is_valid():
			private_key = form.cleaned_data.get('private_key')
			public_key = form.cleaned_data.get('public_key')
			message = form.cleaned_data.get('message')
   
			if private_key:
				original_message = decryption_view(request, private_key, message, *args, **kwargs)
				self.context['result_message'] = original_message 
			elif public_key:
				cipher_message = encryption_view(request, public_key, message, *args, **kwargs)
				self.context['result_message'] = cipher_message
		self.context['form'] = form
		return render(request, self.template_name, self.context)