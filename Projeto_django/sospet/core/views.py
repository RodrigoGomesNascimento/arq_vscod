from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
#importar o autenticate para autenticar através do metodos abaixo
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
#terei com o request todas as requisições enviadas.
from .models import Pet


def login_user(request):
    return render(request, 'login.html')



@login_required(login_url='/login/')#tem que importar e para segurança se nao fica logado sem logar
def list_all_pets(request):
    pet = Pet.objects.filter(active=True) # isso para importar os campos ativos da tabela. E uma query.
    return render(request, 'list.html', {'pet':pet})# tem que colocar no render para poder aparecer.Criando um dicionario.

@login_required(login_url='/login/')
def register_pet(request):
    return render(request, 'register-pet.html')

@login_required(login_url='/login/')
def set_pet(request):
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    city = request.POST.get('city')
    description = request.POST.get('description')
    photo = request.FILES.get('file')
    user = request.user
    pet = Pet.objects.create(email=email, phone=phone, city=city, description=description,photo=photo, user=user)
    url = '/pet/detail/{}/'.format(pet.id)
    return redirect(url)

#nova pagina do cad usuarios.
def list_user_pets(request):
    pet = Pet.objects.filter(active=True, user=request.user)
    return render(request, 'list.html', {'pet':pet})

def pet_detail(request, id):
    pet = Pet.objects.get(active=True, id=id)
    return render(request,'pet.html', {'pet':pet})


def logout_user(request):
    logout(request)
    return redirect('/login/')


@csrf_protect#questão de segurança
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')# se deixar o caminho como no video não vai, pois tem que ser sem o caminho absoluto.

        else:
            messages.error(request, "Usuário e senha inválidos. Favor tentar novamente!")
            return redirect('/login')