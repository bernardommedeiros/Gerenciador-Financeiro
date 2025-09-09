from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from ..services import balancete as service
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.balancete import Balancete


class BalanceteCreateView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'personal_finance/criar_balancete.html')

    def post(self, request):
        balancete = service.criar_balancete(request.user, request.POST)
        return redirect('balancetes_listar')


class BalanceteListView(LoginRequiredMixin, View):
    def get(self, request):
        balancetes = service.listar_balancetes()
        return render(request, 'personal_finance/listar_balancetes.html', {'balancetes': balancetes})
    
class BalanceteDeleteView(LoginRequiredMixin, View):
    def post(self, request, balancete_id):
        balancete = get_object_or_404(Balancete, id=balancete_id)
        service.balancete_delete(balancete_id)
        return redirect('balancetes_listar')
    
class BalanceteUpdateView(LoginRequiredMixin, View):
    def get(self, request, balancete_id):
        balancete = get_object_or_404(Balancete, id=balancete_id)
        return render(request, 'personal_finance/balancete_update.html', {
            'balancete': balancete
        })

    def post(self, request, balancete_id):
        balancete = service.balancete_update(balancete_id, request.POST)
        return redirect('balancetes_listar')