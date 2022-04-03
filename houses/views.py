from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Property
# Create your views here.


def landing(request):
    return render(request, 'landing.html')


def index(request):
    return render(request, 'index.html')


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username is already in use')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is already in use')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'passwords must be equal')
            return redirect('signup')

    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'credentials are not valid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def profile(request, username):

    user = get_object_or_404(User, username=username)

    return render(request, 'profile.html', {
        'username': user,
    })


def property(request, type):

    property = Property.objects.all()

    return render(request, 'property.html', {
        'property': property,
        'type': type,
    })



