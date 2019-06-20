from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views import generic

from .models import BaseCurrency, Currency


def home(request):
    base_list = []
    for base_curr in BaseCurrency.objects.all():
        base_list.append(base_curr.symbol)
    base_list = list(set(base_list))
    context = {
        'base_list': base_list,
    }
    return render(request, 'rates/home.html', context)


def currency(request, base_name):
    currency = {}
    curr_list = ['NZD', 'CAD', 'USD', 'AUD', 'HKD', 'GBP', 'EUR']
    for base_curr in BaseCurrency.objects.filter(symbol=base_name.upper()):
        currency[base_curr] = {}
        for curr in Currency.objects.filter(base=base_curr, symbol__in=curr_list):
            if curr.symbol == base_curr.symbol:
                pass
            else:
                x = {curr: curr.rate_to_base}
                currency[base_curr].update(x)
    context = {
            'base_name': f'{base_name.upper()}',
            'currency': currency
    }
    return render(request, 'rates/currency.html', context)
