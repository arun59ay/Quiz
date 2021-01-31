from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def login_attempt(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email = email).first()
        if not user:
            message = {'error' : 'User does not exsists!'}
            context = message
            return render(request, 'auth/login.html', context)
        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            print("login")
            login(request , user)
            return redirect('/')       
        else:
            # No backend authenticated the credentials
            message = {'error' : 'Invalid Credentials!'}
            context = message
            return render(request, 'auth/login.html', context)

    return render(request, 'auth/login.html')

def register_attempt(request):
    if request.method == "POST":
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email = email).first()

        if user:
            message = {'error' : 'Account already exsists!'}
            context = message
            return render(request, 'auth/register.html', context)

        user = User(first_name= f_name , last_name = l_name , email = email , username=email)
        user.set_password(password)
        user.save()

    return render(request, 'auth/register.html')