from django.shortcuts import render, redirect, get_object_or_404
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
)
from .generateKey import (
    get_generated_key,
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


def encrypt_message_view(request, *args, **kwargs):
    context = {}
    return render(request, 'message.html', context)



def decrypt_message_view(request, *args, **kwargs):
    context = {}
    return render(request, 'message.html', context)