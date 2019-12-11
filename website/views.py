from django.shortcuts import render

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