from django.urls import path

from .views import (
    home_view,
    generate_key_view,
    encrypt_message_view,
    decrypt_message_view,
)



app_name = 'core'

urlpatterns = [
    path('', home_view, name='home'),
    path('update-key/<int:id>/', home_view, name='home'),
    path('generate/key/', generate_key_view, name='generate_key'),
    path('encrypt/', encrypt_message_view, name='encrypt'),
    path('decrypt/', decrypt_message_view, name='decrypt'),
]
