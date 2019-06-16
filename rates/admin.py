from django.contrib import admin
from .models import Currency, BaseCurrency

admin.site.register(Currency)
admin.site.register(BaseCurrency)
