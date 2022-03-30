from django.contrib import admin






from .models import (
    CryptoKey,
    CryptoMessage,
)


# Register your models here.


admin.site.register(CryptoKey)
admin.site.register(CryptoMessage)