from rest_framework.routers import DefaultRouter
from django.urls import path, re_path
from authy.views import *
router = DefaultRouter()
auth_patterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view()),
    path('welcome/', WelcomeUserView.as_view()),
    
]