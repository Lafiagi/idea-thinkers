from rest_framework.routers import DefaultRouter
from django.urls import path, re_path
from authy.views import *
router = DefaultRouter()
auth_patterns = [
    path('api/v1/register/', UserRegistrationView.as_view()),
    path('api/v1/login/', UserLoginView.as_view()),
    path('api/v1/logout/', UserLogoutView.as_view()),
    path('api/v1/welcome/', WelcomeUserView.as_view()),
    
]