# URL mappings for the application
from django.urls import path
from .views import LoginPageView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    #path('login/', LoginPageView.as_view(), name='login'),
    ]