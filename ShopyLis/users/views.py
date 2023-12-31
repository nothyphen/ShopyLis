from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission

# Create your views here.
def login_system(request):
    if request.user.is_authenticated:
        return redirect('/user/account/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/user/account/')
            else:
                return redirect('/user/login/')
        template = 'login_page.html'
        return render(request, template)

def logout_system(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/')

def register(request):
    if request.user.is_authenticated:
        return redirect('/user/account')
    else:
        try:
            if request.methode == 'POST':
                email = request.POST['email']
                username = request.POST['username']
                password = request.POST['password']
                user = User.objects.create_user(username, email, password)
                user.save()
                return redirect('/user/login')
        except:
            template = '404.html'
            return render(request, template)
    template = 'register.html'
    return render(request, template)

def forgetpassword(request):
    pass

def changepassword(request):
    pass

def verify(request):
    pass

def account(request):
    pass