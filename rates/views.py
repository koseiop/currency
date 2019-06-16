from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import BaseCurrency, Currency


def index(request, base_name):
    currency = BaseCurrency.objects.get(symbol=base_name.upper())
    qs = Currency.objects.filter(Q(date__contains=currency.date) and Q(base__contains=currency))
    context = {
        'currency': currency,
        'qs': qs
    }
    return render(request, 'home.html', context)
