from django.views.generic.base import TemplateView
from django.shortcuts import render

from suiterest.suitecrmapi import SuitCrmApi
from suiterest.cryptoapi  import CryptoCurrencies

# Create your views here.
class HomeView(TemplateView):
    template_name = 'suiterest/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        data = SuitCrmApi().getData()
        context['data'] = data['entry_list']
        return context

class Cryptoview(TemplateView):
    template_name = 'suiterest/crypto.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Cryptoview, self).get_context_data(*args, **kwargs)
        data = CryptoCurrencies().get_crypto_price(cur_symbol = 'BTC', exchange = 'USD', start_date = '2022-01-01')
        context['data'] = data
        return context
