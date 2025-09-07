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
        return redirect('balancete_listar')


class BalanceteListView(LoginRequiredMixin, View):
    def get(self, request):
        balancetes = service.listar_balancetes()
        return render(request, 'personal_finance/listar_balancetes.html', {'balancetes': balancetes})