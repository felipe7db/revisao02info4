from django.shortcuts import render

def inicial(request):
    return render(request, 'index.html')

def sucesso(request):
    return render(request, 'sucesso.html')

def avaliacao(request):
    nome = request.POST['nome']
    comentario = request.POST['comentario']
    nota = request.POST['nota']

    if len(nome) >= 3 and len(comentario) >= 10 and 1 <= int(nota) <=5:
        context = {
            'nome': nome,
            'comentario': comentario,
            'nota': nota
        }
        return render(request, 'sucesso.html', context)
    else:
        return render(request, 'index.html')