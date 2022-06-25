# URL mappings for the application
from django.urls import path
from .views import LoginPageView, HomePageView, ProfilePageView, HistoryPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('profile/', ProfilePageView.as_view(), name = 'profile'),
    path('history/', HistoryPageView.as_view(), name = 'history'),
    ]
