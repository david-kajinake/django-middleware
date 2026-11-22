from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'app/index.html')
    messages.info(request, 'You must login')
    return redirect('user_login')

def user_login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user= authenticate(username= username, password= password)
        if user is not None:
            login(request,user)
            return redirect('home')
        messages.info(request, 'Wrong username or password')
    return render(request, 'app/login.html')

def user_logout(request):
    if request.method== 'POST':
        logout(request)
        messages.info(request, 'You have logged out.')
        return redirect('user_login')

