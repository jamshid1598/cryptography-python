from django.urls import path

from .views import (
    generate_key,
    encrypt_message,
    decrypt_message,
)



app_name = 'core'

urlpatterns = [
    path('', generate_key, name='key'),
    path('encrypt/', encrypt_message, name='encrypt'),
    path('decrypt/', decrypt_message, name='decrypt'),
]
