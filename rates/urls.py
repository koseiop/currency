from django.urls import path

from . import views
from .models import Currency

app_name = 'rates'
urlpatterns = [
    # path('', views.HomeView.as_view(), name='home',),
    path('', views.home, name='home',),
    path('<str:base_name>/', views.currency, name='latest currency data'),
]
