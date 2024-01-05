from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from core.models import *


def login_(request):
    if not request.user.is_authenticated:
        msg = ""
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('HOME')
            else:
                msg = "something wrong!! please try again."

        context = {
            'msg': msg
        }
        return render(request,"account/login.html",context)
    else:
        return redirect('HOME')


def registration(request):
    if not request.user.is_authenticated:
        msg = ""
        if request.method == "POST":
            first_name = request.POST.get('first-name')
            last_name = request.POST.get('last-name')
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_valid_check = User.objects.filter(username=username).exists()
            if user_valid_check :
                msg = 'User name or Email already exist!!'
                return redirect("login")
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name,username=username,password=password)
                user.save()
                login(request, user)
                return redirect("login")
        context = {
            'msg': msg
        }
        return render(request,"account/login.html",context)
    else:
        return redirect('my-account')

def my_account(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        orders = Order.objects.filter(user=request.user)
        customer = Customer.objects.filter(user=request.user).last()
        print(customer)
        context ={
            'navbar':'my_account',
            'cart':cart,
            'orders':orders,
            'customer':customer
        }
        return render(request,"account/my_account.html",context)
    else:
        return redirect("login")


def signout(request):
    logout(request)
    return redirect("HOME")