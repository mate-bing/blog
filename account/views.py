from django.shortcuts import render
from django.http import  HttpResponse
from django.contrib.auth import authenticate,login
from  .forms import  LoginForm


def user_login(request):
    if request.method== "POST":
        login_form =LoginForm(request.POST)
        #这是一个坑，必须填
        if login_form.is_valid():
            cd =login_form.cleaned_data
            user =authenticate(username=cd ['username'],password=cd ['password'])

            if user :
                login(request,user)
                return HttpResponse("Welcome you. You have been authenticated successful")
            else:
                return  HttpResponse("Sorry.Your username or password is not right")
        else:
            return  HttpResponse("Invalid login")
    if request.method=="GET":
        login_form =LoginForm()
        return  render(request,"account/login.html",{"from":login_form})