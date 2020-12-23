from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

from .models import Customer
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from .forms import *

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

def dashboard(request,pk):
    user = User.objects.filter(id=pk)[0]
    customer = Customer.objects.filter(username=user.username)[0]
    # customer = Customer.objects.filter(username = user.username)
    print(customer.phone)
    print("+++++++++++++++++++++++++++++++++")
    print(user.email)
    return render(request, 'customer/dashboard.html',{'customer':customer})

def editProfile(request):
    username = request.user
    customer = Customer.objects.get(email=username.email)
    oldpass=customer.password
    userform = UserForm(instance=username)
    customerform = CustomerEditForm(instance=customer)
    if request.method =="POST":
        user = UserForm(request.POST,instance=username)
        customer = CustomerEditForm(request.POST,request.FILES,instance=customer)
        if user.is_valid() and customer.is_valid():
            udetails=user.save(commit=False)
            cdetails=customer.save(commit=False)
            cdetails.username=udetails.username
            cdetails.first_name=udetails.first_name
            cdetails.last_name=udetails.last_name
            cdetails.email = udetails.email
            if oldpass!=cdetails.password:
                udetails.set_password(cdetails.password)
                udetails.save()
                cdetails.save()
                messages.success(request, 'Your password was successfully updated!')
            else:
                udetails.save()
                cdetails.save()
            authenticate(username = cdetails.username,password = cdetails.password)
            login(request,udetails)    
            
        return redirect('customer-dashboard', pk = username.id)
        
    return render(request , 'customer/edit_profile.html',{'userform':userform,'customerform':customerform})  


def timeline(request):
    return render(request, 'customer/timeline.html')   
