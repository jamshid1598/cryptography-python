from django.urls import path, include

# local files
from .views import (
    login_view,
    logout_view,
    signup_view,
    SignUpView,
)

app_name = "user"

urlpatterns = [
    # api routes for authentication
    path("api.auth/", include("apps.users.api.urls", namespace="auth_api")),
    
    # 
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    
    
]
