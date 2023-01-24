from django.urls import path
from .views import OrderAPIView

app_name = 'authentication'

urlpatterns = [
    # path('users/', UserRetrieveUpdateAPIView.as_view()),
    path('orders/', OrderAPIView.as_view()),
   
]