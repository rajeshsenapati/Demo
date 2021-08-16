from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import PostModel
from .forms import PostForm

# Create your views here.


def sign_up(request):
    if request.method == "POST":
        fm = UserForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Successfully SignUp !!')
            fm.save()
    else:
        fm = UserForm()
    return render(request, 'signup.html', {"form": fm})


def log_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                user_name = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=user_name, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('post')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return redirect('post')

# Authenticate for Anonymous user


def post(request):
    if request.user.is_authenticated:
        fm = PostForm(request.POST)
        if request.method == "POST":
            fm.save()
            return redirect('post')
        all_post = PostModel.objects.all()
        return render(request, 'post.html', {"name": request.user, "post": all_post, "form": fm})
    else:
        return redirect('login')


def user_logout(request):
    logout(request)
    return redirect('login')

