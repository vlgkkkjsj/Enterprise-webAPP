from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import Q

def home(request):
    users = User.objects.all()
    cookie_value = request.COOKIES.get('user_username', 'Visitante')
    return render(request, "index.html", {"users": users, "cookie_value": cookie_value})

@login_required
def cadastrar(request):
    users = User.objects.all()
    return render(request,"cadastro.html", {"users": users})


@login_required
def salvar(request):
   
   nickname = request.POST.get("nickname")  
   name = request.POST.get("name")
   gender = request.POST.get("gender")  
   age = request.POST.get("age")   
   
   User.objects.create(nickname=nickname, name=name , gender=gender, age=age)
   return redirect(listar)

def editar(request, id):
    user = User.objects.get(id=id)
    return render(request, "listar.html", {"user": user})

@login_required
def update(request, id):
    nickname = request.POST.get("nickname")
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    age = request.POST.get("age")

    user = User.objects.get(id=id)
    user.nickname = nickname
    user.name = name
    user.gender = gender
    user.age = age
    user.save()
    return redirect(listar)

@login_required
def listar(request):
    users= User.objects.all()
    query = request.GET.get('q')

    if query:
        users = users.filter(Q(name__icontains=query))

    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
    }
    return render(request, 'listar.html', context)

def homeLogin(request):
    if request.user.is_authenticated:
        return redirect(homeLog)
    else:
        return redirect(login)

@login_required
def homeLog(request):
    users = User.objects.all()
    return render(request, 'logged.html', {"users": users})

@login_required
def homeDashboard(request):
    return redirect(listar)

@login_required
def delete(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect(listar)

def login(request):
    return render(request, "login.html")

def logar(request):
    if request.method == "POST":
        username = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            response = redirect(homeLog)
            response.set_cookie('user.username', user.username, max_age=3600)  # Define o cookie com o nome do usuário
            return response
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

def custom_logout(request):
    
    response = redirect(home)
    response.delete_cookie('user_username')  # Remove o cookie ao fazer logout
    logout(request)
    return response
