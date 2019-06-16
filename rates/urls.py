from django.urls import path

from . import views
from .models import Currency

app_name = 'rates'
urlpatterns = [
    path('', views.index, name='home'),
]
