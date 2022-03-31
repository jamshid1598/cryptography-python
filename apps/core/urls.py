from django.urls import path

from .views import (
    home_view,
    generate_key_view,
    encryptDecryptView,
    EncryptDecryptView
)



app_name = 'core'

urlpatterns = [
    path('', home_view, name='home'),
    path('update-key/<int:id>/', home_view, name='home'),
    path('generate/key/', generate_key_view, name='generate_key'),
    path('encrypt-decrypt/', EncryptDecryptView.as_view(), name='encrypt_decrypt'),
]
