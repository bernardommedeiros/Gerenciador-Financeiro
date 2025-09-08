from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from ..forms import UserRegisterForm, UserLoginForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listar_balancetes') 
        else:
            print(form.errors)  
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('listar_balancetes')
    else:
        form = UserLoginForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')