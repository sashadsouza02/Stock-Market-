from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def homepage(request):
    return render(request,'market/homepage.html')

def stocks(request):
    stockslist = Stock.objects.orderby('symbol')
    context = {'stockslist':stockslist}
    return render(request, 'market/stocks.html',context}
    
def register(request):
    username = request.POST['username']
    password = request.POST['password']
    balance = request.POST['balance']
    
    
    
    
def loginpage(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('home')
        else:
            return render(request,'market/login.html',{'error':"The user account is inactive"})
    else:
        return render(request,'market/login.html',{'error':"Please enter correct username/password"})

# Create your views here.
