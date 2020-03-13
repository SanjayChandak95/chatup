from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
#signal
from django.db.models.signals import post_save

#django Channel

# Create your views here.
from .models import *
from .forms import *
from django.db.models import Q
#from validation.EmailValidation import *

def signUp_view(request,*args,**kwargs):
    if "user" in request.COOKIES:
        response = HttpResponseRedirect("../signUp")
        response.delete_cookie('user')
        return response
    if request.method == "POST":
        signUp = SignUpForm(request.POST)
        if signUp.is_valid():
            signUp.save()
            return HttpResponseRedirect("../login")
        else:
            messages.error(request,"Error")
    signUp = SignUpForm()
    return render(request,"signUpForm.html",{'signUp' : signUp})

def login_view(request,*args,**kwargs):
    if "user" in request.COOKIES:
        response = HttpResponseRedirect("../welcome")
        response.delete_cookie('user')
        return response
    if request.method == "POST":
        login = LoginForm(request.POST)
        if login.is_valid():
            email = login.cleaned_data['email']
            pwd = login.cleaned_data['password']
            validUser = User.objects.filter(email = email).filter(password = pwd)
            if len(validUser) == 1:
                #need session to check from now that user have logged in
                response = HttpResponseRedirect("../welcome")
                response.set_cookie('user',email)
                return response
    login = LoginForm()
    return render(request,"login.html",{'login' : login})


def home_view(request,*args,**kwargs):
    if "user" in request.COOKIES:
        email = request.COOKIES["user"]
        #currentUser = user.objects.filter(email = email).first()
        users = User.objects.exclude(email = email).all()
        return render(request,"application.html",{'users':users,'email':email})
    else:
        return HttpResponseRedirect("../login")
    #return HttpResponse("<a href = \"../welcome\">Welcome to GroceryList Editor Version 1.0  </a>")

def chat_view(request,id,*args,**kwargs):
    if "user" in request.COOKIES:
        email = request.COOKIES["user"]
        users = User.objects.exclude(email = email).all()
        sender = User.objects.filter(email = email).first()
        reciever = User.objects.get(id = id)
        chatTableForm =ChatTableForm()
        if request.method =="POST":
            chatTableForm = ChatTableForm(request.POST)
            if chatTableForm.is_valid():
                ChatTable.objects.create(sender = sender, reciever = reciever,message =chatTableForm.cleaned_data["message"])
        chatHistories = (ChatTable.objects.filter(sender = sender, reciever = reciever) | ChatTable.objects.filter(sender = reciever, reciever = sender)).order_by('id')
        if len(chatHistories) == 0:
            chatHistories = None
        else:
            chatHistories = chatHistories.all()
        chatTableForm =ChatTableForm()
        return render(request,"chat.html",{'chatTableForm':chatTableForm,'chatHistories':chatHistories,'reciever':reciever,'users':users,'email':email})
    else:
        return HttpResponseRedirect("../login")

def logout_view(request,*args,**kwargs):
    response = HttpResponseRedirect("../welcome")
    response.delete_cookie('user')
    return response
