from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .models import Currency

app_name = 'rates'
urlpatterns = [
    # path('', views.HomeView.as_view(), name='home',),
    path('', views.home, name='home',),
    path('<str:base_name>/', views.currency, name='latest currency data'),
]

# Serve static files for use in web pages
urlpatterns += staticfiles_urlpatterns()
