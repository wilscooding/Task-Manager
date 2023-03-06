from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    context = {"form": form}

    return render(request, "accounts/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")


def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            password_confirmation = form.cleaned_data.get(
                "password_confirmation"
            )
            if password == password_confirmation:
                user = User.objects.create_user(username, password=password)
                login(request, user)
                return redirect("list_projects")
            else:
                form.add_error(None, "Passwords do not match.")
    else:
        form = SignupForm()
        context = {"form": form}
        return render(request, "accounts/signup.html", context)
