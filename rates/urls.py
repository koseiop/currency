from django.urls import path

from . import views
from .models import Currency

app_name = 'rates'
urlpatterns = [
    path('<str:base_name>/', views.index, name='home'),
]
