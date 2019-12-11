from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.

def index(request):
   
    return render(request, 'index.html')

def home(request):

    return render(request, 'home.html')

def contato(request):

    return render(request, 'contact.html')

def sobre(request):

    return render(request, 'about2.html')

def preco(request):

    return render(request, 'pricing.html')

def servico(request):

    return render(request, 'service.html')

def time(request):

    return render(request, 'team.html')

def login_user(request):

    return render(request, 'login.html')

def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')


def cadastro_Mensagem(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        context = {
            'msg': "Pedido realizado com sucesso"
        }
        return render(request, 'contact.html', context)
    context = {
        'formulario':form
    }

    return render(request, 'contact.html', context)

class register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha inválidos. Favor tentar novamente!')
    return redirect('/login/')

