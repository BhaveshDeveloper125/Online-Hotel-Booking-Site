from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2 :
            if User.objects.filter(username = username).exists():
                messages.info(request , 'User Name you entered is already registered please use another  User name')
                return redirect('/')
            elif  User.objects.filter(email = email):
                messages.info(request , 'Email you entered are already registered please use another email')
                return redirect('/')
            else:
                user = User.objects.create_user(first_name = first_name , last_name = last_name , username = username ,email=email , password = password1)
                user.save()
                return redirect('/')
        else:
             messages.info(request ,'Password is not matching please enter vliad password in both field')
             return redirect('/')
    else:
        return render(request,'/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)

        if user is not None and user.is_staff == False:
            auth.login(request , user)
            return redirect('/')
        else:
            messages.info(request , 'Invalid Username or password')
            return redirect('/')
    else:
        return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')


def forgot(request):
    if request.method == 'POST':
        forgotten_email = request.POST['forgotten_email']
        user = User.objects.filter(email=forgotten_email).first()

        if user:
            print(user.password)  
            return HttpResponse('Email exists')
        else:
            return HttpResponse('Email does not exist')

        