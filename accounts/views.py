from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def login(request):
    if request.method == "GET":
        return render(request, 'accounts/pages/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            return HttpResponse ('Você entrou com sucesso')
        else:
            return HttpResponse('ERRO: login não existe na base de dados')
        
def cadastro(request):
    if request.method == "GET":
        return render(request, 'accounts/pages/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com este nome')
        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha)
        user.save()
        
        return HttpResponse('Usuário cadastrado com sucesso')


        

# Create your views here.
