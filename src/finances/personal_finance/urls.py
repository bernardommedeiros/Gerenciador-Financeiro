from django.urls import path
from django.contrib.auth import views as auth_views
from .views.auth import register_view, login_view, logout_view
from .views.balancete import BalanceteListView, BalanceteCreateView
from .views.boleto import BoletoListView, BoletoCreateView



urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    
    path('balancetes/novo/', BalanceteCreateView.as_view(), name='balancete_criar'),
    path('/home/', BalanceteListView.as_view(), name='listar_balancetes'),
    path('balancete/<int:balancete_id>/boletos/', BoletoListView.as_view(), name='boleto_listar'),
    path('balancete/<int:balancete_id>/boletos/novo/', BoletoCreateView.as_view(), name='boleto_criar')
]