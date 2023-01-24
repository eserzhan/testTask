from django.urls import path

from .views import (
    RegistrationAPIView,
    GetProfile
)

app_name = 'authentication'

urlpatterns = [
    path('users/registration/', RegistrationAPIView.as_view()),
    path('users/', GetProfile.as_view()),
]