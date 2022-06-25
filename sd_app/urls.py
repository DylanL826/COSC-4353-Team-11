# URL mappings for the application
from django.urls import path
from .views import LoginPageView, HomePageView, ProfilePageView, buyPage, registerPage

app_name = "sd_app"

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('profile/', ProfilePageView.as_view(), name = 'profile'),
    path('buy/', buyPage, name='buy'),
    path("register/", registerPage, name="register"),
    ]