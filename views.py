from django.shortcuts import render, redirect
from .models import Receipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
# Create your views here.


#receipe page


def receipe(request):
    if request.method=="POST":
        data=request.POST
        
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get("receipe_image")
        
        Receipe.objects.create(
           
           receipe_name=receipe_name,
           receipe_description=receipe_description,
           receipe_image=receipe_image
       )
        return redirect('/receipe/')
    
    
    queryset=Receipe.objects.all()
    context ={'queryset':queryset}
    return render(request, "receipe.html" , context )


# login 


def login_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        if not User.objects.filter(username= username).exists():
            messages.error(request , "Invalid username")
            return redirect('/login/')
        user= authenticate(username = username, password = password)
        
        if user is None:
            messsag.error(request , "Invalid Crediatail")
            
        else:  #  session page redirect by it 
            login(request, user)
            return redirect('/receipe/')    
    return render(request, 'login.html')


# register page 


def register_page(request):
    
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        user = User.objects.create(
          first_name=first_name,
           last_name=last_name,
           username=username)
        user.set_password(password)
        user.save()
    
        
        return redirect('/register_page/')
    return render(request, 'register.html')