from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
from datetime import date

def inicial(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def sucesso(request):
    nome = request.POST['nome']
    email = request.POST['email']
    data = request.POST['data']
    
    # Converte a string para um objeto de data
    data_nasc = date.fromisoformat(data)
    
    # Pega a data de hoje
    hoje = date.today()
    
    # Calcula a diferença de anos
    idade = hoje.year - data_nasc.year

    if len(nome) >= 3 and "@" in email and idade >= 18:
        context = {
            'nome': nome,
            'email': email,
            'data': data
        }
        return render(request, 'sucesso.html', context)
    else:
        return render(request, 'cadastro.html')