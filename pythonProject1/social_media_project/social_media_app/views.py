# social_media_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile, Post, Message
# social_media_app/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'user': request.user})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(user=user)
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')

# Implement views for forgot password, posts, following, followers, and messages
