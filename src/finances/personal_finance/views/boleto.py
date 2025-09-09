from django.views import View
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from ..services import boleto as service
from ..models.balancete import Balancete
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

class BoletoCreateView(LoginRequiredMixin, View):
    def get(self, request, balancete_id):
        return render(request, 'personal_finance/criar_boletos.html', {
            'balancete_id': balancete_id
        })

    def post(self, request, balancete_id):
        boleto = service.criar_boleto(request.POST, request.FILES, balancete_id=balancete_id)
        return redirect('boleto_listar', balancete_id=balancete_id)


class BoletoListView(LoginRequiredMixin, ListView):
    template_name = 'personal_finance/listar_boletos.html'
    context_object_name = 'boletos'
    
    def get(self, request, *args, **kwargs):
        balancete_id = kwargs.get('balancete_id')
        if not balancete_id:
            raise Http404("Balancete não especificado.")
        
        balancete = get_object_or_404(Balancete, id=balancete_id)

        boletos = service.listar_boletos(balancete_id=balancete_id)
        dados = service.calcular_saldo(balancete_id=balancete_id)    

        return render(request, self.template_name, {
            'boletos': boletos,
            'saldo': dados['saldo'],
            'faturamento': dados['faturamento'],
            'despesa': dados['despesa'],
            'balancete': balancete,
        })
    
class BoletoDeleteView(LoginRequiredMixin, View):
    def post(self, request, boleto_id):
        boleto = get_object_or_404(service.listar_boletos(), id=boleto_id)
        balancete_id = boleto.balancete.id
        service.boleto_delete(boleto_id)
        return redirect('boleto_listar', balancete_id=balancete_id)
    
class BoletoUpdateView(LoginRequiredMixin, View):
    def get(self, request, boleto_id):
        boleto = get_object_or_404(service.listar_boletos(), id=boleto_id)
        return render(request, 'personal_finance/boleto_update.html', {
            'boleto': boleto
        })

    def post(self, request, boleto_id):
        boleto = service.boleto_update(boleto_id, request.POST, request.FILES)
        return redirect('boleto_listar', balancete_id=boleto.balancete.id)