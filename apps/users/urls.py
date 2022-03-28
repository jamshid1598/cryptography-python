from django.urls import path, include

app_name = "account"

urlpatterns = [
    # api routes for authentication
    path("api.auth/", include("apps.users.api.urls", namespace="auth_api")),
]
