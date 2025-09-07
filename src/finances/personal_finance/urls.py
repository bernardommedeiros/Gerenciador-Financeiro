from django.urls import path
from django.contrib.auth import views as auth_views
from .views.auth import register_view, login_view
from .views.balancete import BalanceteListView, BalanceteCreateView


urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    
    path('balancetes/novo/', BalanceteCreateView.as_view(), name='balancete_criar'),
    path('', BalanceteListView.as_view(), name='listar_balancetes'),
]