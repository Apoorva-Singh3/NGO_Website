from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

def home(request):
    return render(request,'index.html',{})

def backend(request):
    return render(request,'backend.html',{})

def Login(request):
    return render(request, 'login.html',{})
    # if request.user.is_authenticated:
    #     return render(request, 'backend.html')
    # else:
    #     messages.info(request,'Please login to access this page.')
    #     return HttpResponseRedirect('/')
    
def LoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect('/backend')
        else:
            messages.error(request,'Enter your data correctly.')
            return HttpResponseRedirect('/')

def LogoutUser(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect('/')
