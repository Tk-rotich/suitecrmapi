from django.views.generic.base import TemplateView
from django.shortcuts import render

from suiterest.suitecrmapi import SuitCrmApi

# Create your views here.
class HomeView(TemplateView):
    template_name = 'suiterest/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        data = SuitCrmApi().getData()
        context['data'] = data['entry_list']
        return context
