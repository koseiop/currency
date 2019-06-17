from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views import generic

from .models import BaseCurrency, Currency


# class HomeView(generic.ListView):
#     template_name = 'rates/home.html'
#     context_object_name = 'base_list'
#
#     def get_queryset(self):
#         """
#         Returns all BaseCurrency objects in the database
#         """
#         return list(set(BaseCurrency.objects.order_by('symbol')))

def home(request):
    base_list = []
    for base_curr in BaseCurrency.objects.all():
        base_list.append(base_curr.symbol)
    base_list = list(set(base_list))
    print(base_list, "hjfjhasgfasjf")
    context = {
        'base_list': base_list,
    }
    return render(request, 'rates/home.html', context)
def currency(request, base_name):
    # currency = BaseCurrency.objects.filter(symbol=base_name.upper())
    # qs = Currency.objects.filter(Q(date__contains=currency[0].date) and Q(base__contains=currency[0]))
    # context = {
    #     'currency': currency,
    #     'qs': qs
    # }
    currency = {}
    for base_curr in BaseCurrency.objects.filter(symbol=base_name.upper()):
        currency[base_curr] = {}
        for curr in Currency.objects.filter(date=base_curr.date, base=base_curr):
            if curr.symbol == base_curr.symbol:
                pass
            else:
                x = {curr: curr.rate_to_gbp}
                currency[base_curr].update(x)
    context = {
            'base_name': f'{base_name.upper()}',
            'currency': currency
    }
    return render(request, 'rates/currency.html', context)
