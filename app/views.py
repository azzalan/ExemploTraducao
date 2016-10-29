from django.shortcuts import render
from django.views.generic import TemplateView

from app.models import Exemplo

class ExemploView(TemplateView):
    template_name = 'template_exemplo.html'

    def get_context_data(self, **kwargs):
        context = super(ExemploView, self).get_context_data(**kwargs)
        context['exemplo_no_contexto'] = Exemplo.objects.all()
        return context
