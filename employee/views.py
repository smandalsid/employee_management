from django.shortcuts import render, redirect
from django.contrib import messages
from employee.models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def registration(request):
    if request.method=="POST":
        print("HELLO")
        fname=request.POST['fname']
        lname=request.POST['lname']
        eid=request.POST['eid']
        email=request.POST['email']
        password=request.POST['pass']

        try:
            user=User.objects.create(first_name=fname, last_name=lname, username=email, password=password)
            Employee.objects.create(user=user, eid=eid)
            messages.success(request, "Registered successfully")
            return redirect('login')
        except:
            messages.success(request, "Error...")
    return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')