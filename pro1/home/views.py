from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=="POST":
        
        email=request.POST['email']
        passw=request.POST['password']
        cpassw=request.POST['cpassword']
        if passw==cpassw:
            if RegisterUser.objects.filter(email=email).exists():
                messages.info(request,'Email exists')
                return redirect(register)
            else:
                print("r")
                query=RegisterUser.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],uname=request.POST['uname'],email=email,password=passw)
                # query.set_password(passw)
                query.save()
                return redirect(login)
        else:
            messages.info(request,"Both Passwords dont match")
            return redirect(register)
    return render(request,'register.html')
def login(request):
    if request.method=="POST":
        query=auth.authenticate(email=request.POST['email'],password=request.POST['password'])
        if query is None:
            messages.info(request,"Invalid credentials")
            return redirect(login)
        else:
            auth.login(request,query)
            return redirect(index)
    else:
        return render(request,'login.html')
