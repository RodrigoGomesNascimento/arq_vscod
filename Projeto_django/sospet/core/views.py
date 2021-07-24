from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
#importar o autenticate para autenticar através do metodos abaixo
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
#terei com o request todas as requisições enviadas.



def login_user(request):
    return render(request, 'login.html')



@login_required(login_url='/login')#tem que importar e para segurança se nao fica logado sem logar
def index(request):
    return render(request, 'index.html')

def list_all_pets(request):
    return render(request, 'list.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')


@csrf_protect#questão de segurança
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')# se deixar o caminho como no video não vai, pois tem que ser sem o caminho absoluto.

        else:
            messages.error(request, "Usuário e senha inválidos. Favor tentar novamente!")
            return redirect('/login')