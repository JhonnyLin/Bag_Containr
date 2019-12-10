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