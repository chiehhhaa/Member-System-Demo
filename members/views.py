from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUP


def login_user(req):
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(req, username=username, password=password)
        if user is not None and user.is_active:
            login(req, user)
            return redirect("home")
        else:
            messages.success(req, "帳號/密碼不正確")
            return redirect("login")
    else:
        return render(req, "registration/login.html")


def logout_user(req):
    logout(req)
    messages.success(req, "登出成功！")
    return redirect("home")


def register_user(req):
    if req.method == "POST":
        form = SignUP(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "註冊成功！")
            return redirect("login")
    else:
        form = SignUP()
    return render(req, "registration/register.html", {"form": form})
