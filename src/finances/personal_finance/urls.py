from django.urls import path
from django.contrib.auth import views as auth_views
from .views.auth import register_view, login_view, logout_view
from .views.balancete import BalanceteListView, BalanceteCreateView, BalanceteDeleteView, BalanceteUpdateView
from .views.boleto import BoletoListView, BoletoCreateView, BoletoDeleteView, BoletoUpdateView



urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    
    path('balancetes/novo/', BalanceteCreateView.as_view(), name='balancete_criar'),
    path('home/', BalanceteListView.as_view(), name='balancetes_listar'),
    path('balancete/<int:balancete_id>/delete/', BalanceteDeleteView.as_view(), name='balancete_delete'),
    path('balancete/<int:balancete_id>/edit/', BalanceteUpdateView.as_view(), name='balancete_update'),
    
    path('balancete/<int:balancete_id>/boletos/', BoletoListView.as_view(), name='boleto_listar'),
    path('balancete/<int:balancete_id>/boletos/novo/', BoletoCreateView.as_view(), name='boleto_criar'),
    path('boleto/<int:boleto_id>/delete/', BoletoDeleteView.as_view(), name='boleto_delete'),
    path('boleto/<int:boleto_id>/edit/', BoletoUpdateView.as_view(), name='boleto_update'),
]