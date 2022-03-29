from django.shortcuts import render
from django.views.generic import (
    CreateView, 
    UpdateView,
)

# CRYPTOGRAPHY
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Create your views here.

from .models import (
    CryptoKey,
    CryptoMessage,
)



def generate_key(request, *args, **kwargs):
    context = {}
    template_name='crytokey.html'
    
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=1024,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    
    context['private_key'] = private_key
    context['public_key'] = public_key
    return render(request, template_name, context)



def encrypt_message(request, *args, **kwargs):
    context = {}
    return render(request, 'message.html', context)



def decrypt_message(request, *args, **kwargs):
    context = {}
    return render(request, 'message.html', context)