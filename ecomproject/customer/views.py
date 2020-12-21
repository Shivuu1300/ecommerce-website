from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Customer
from django.contrib.auth import login,logout,authenticate
from .forms import CustomerGetStartedForm

# This is for landing page of the entire website
def home(request):
    return render(request, 'customer/index.html')
def getstarted(request):
    form = CustomerGetStartedForm
    if request.method == 'POST':
        form = CustomerGetStartedForm(request.POST, request.FILES)
        
        if form.is_valid():

            username = form['username'].value()
            password = form['password'].value()
            email= form['email'].value()
            first_name=form['first_name'].value()
            last_name=form['last_name'].value()
            #print(username,email,password)
            newuser = User.objects._create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            print(newuser)
            newuser.save() # User is being added to the user model

            form.save() #Customer-type User is being added to the customer model
            login(request, newuser)
            messages.success(request, 'New User created!')
            return render(request, 'customer/index.html')
    return render(request, 'customer/getstarted.html',{'form':form})

def logIn(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        print(user)
        if user is not None:
            login(request,user)
            messages.info(request,'Login Successful!')
            return redirect("customer-home")
        else:
            messages.info(request,'Username or Password is incorrect')

    return render(request, 'customer/login.html')

def logOut(request):
    logout(request)
    messages.info(request,'Logout Successful!')
    return redirect("customer-home") 

def userProfile(request,pk):
    user = User.objects.filter(id=pk)[0]
    
    customer = Customer.objects.filter(username = user.username)
    print(customer)
    return redirect("customer-home")
