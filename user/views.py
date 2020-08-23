from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
#from django.contrib.auth import login, authenticate
from django.contrib import auth

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        auth.login(request,newUser)
        #messages.success(request,message="Başarıyla Kayıt Oldunuz.")
        messages.info(request, message="Başarıyla Kayıt Oldunuz.")
        #log = login(request)
        
        return redirect("index")
    
    context = {
        "form": form
    }
    return render(request, "register.html", context)

def login(request):
    login_form = LoginForm(request.POST or None)

    context = {
        "form": login_form
    }

    if login_form.is_valid():
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = auth.authenticate(username= username, password= password)
        if user is None:
            messages.info(request,"Kullanıcı adı veya parola hatalı.")
            return render(request, "login.html", context= context)

        messages.success(request, message="Başarıyla giriş yaptınız.")
        auth.login(request, user)
        return redirect("index")

    return render(request, "login.html", context= context)

def logoutUser(request):
    auth.logout(request)
    messages.success(request, message="Başarıyla çıkış yaptınız.")
    return redirect("index")


