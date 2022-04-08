from django.views.generic.base import TemplateView
from django.views.generic import FormView, ListView
from django.views.generic import View
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from suiterest.suitecrmapi import SuitCrmApi
from suiterest.cryptoapi  import CryptoCurrencies
from suiterest.forms import StartDateForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'suiterest/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        data = SuitCrmApi().getData()
        context['data'] = data['entry_list']
        return context

# class Cryptoview(TemplateView, FormView):
#     template_name = 'suiterest/crypto.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super(Cryptoview, self).get_context_data(*args, **kwargs)
#         data = CryptoCurrencies().get_crypto_price(cur_symbol = 'BTC', exchange = 'USD', start_date = '2022-01-01')
#         context['data'] = data
#         return context


class Cryptoview(TemplateView):
    template_name = "suiterest/crypto.html"

    def get_context_data(self, *args, **kwargs):
            context = super(Cryptoview, self).get_context_data(*args, **kwargs)
            data = CryptoCurrencies().get_crypto_price(cur_symbol = 'BTC', exchange = 'USD', start_date = '2022-01-01')
            context['data'] = data
            return context

    def get(self, request):
        form = StartDateForm()
        data = CryptoCurrencies().get_crypto_price(cur_symbol = 'BTC', exchange = 'USD', start_date = '2022-01-01')
        return render(request, self.template_name, {"form": form, 'data':data})

    def post(self, request):
        form = StartDateForm(request.POST)
        print(request.POST.get('start_date'))
        if form.is_valid():
            from_date = str(form.cleaned_data['start_date'])
            print(type(from_date))
            data = CryptoCurrencies().get_crypto_price(cur_symbol = 'BTC', exchange = 'USD', start_date = from_date)
            return render(request, self.template_name, {"form": form, "data": data })
        data = CryptoCurrencies().get_crypto_price(cur_symbol = 'BTC', exchange = 'USD', start_date = '2022-01-01')
        return render(request, self.template_name, {"form": form, 'data': data})
