from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.
def signup(request):
    return render(request, 'user_app/signup.html')

def register(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    user = User.objects.create_user(username, email, password)

    print(user)

    return HttpResponseRedirect(reverse('user_app:login_page'))

def login_page(request):
    return render(request, 'user_app/login.html')

def login_form(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect(reverse('user_app:home'))
    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect(reverse('user_app:login_page'))

def home(request):
    return render(request, 'user_app/home.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('posts:index'))
