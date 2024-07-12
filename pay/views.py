from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf import settings
import re
from django.views.decorators.cache import cache_control
from . import name

@cache_control(no_cache=True, must_revalidate=True, max_age=0)








# Create your views here.
def land(request):
    return render(request,'landingPage.html',{})


def Login(request):
    if request.method == 'POST':
        usn = request.POST['username']
        passw = request.POST['password']
        name.user_name(usn)

        User = auth.authenticate(username=usn, password=passw)
        if User is not None:
            auth.login(request, User) 
            return render(request,'home.html',{'username':usn,})
        else:
            messages.error(request, 'Invalid Credentials. Please check.')
    
    return render(request, 'loginPage.html',{'username':usn, })


def Register(request):
    
    if request.method == 'POST':
        usn = request.POST['username']
        email = request.POST['email']
        passw = request.POST['password']
        name.user_name(usn)

        if not re.match(r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email): 
            messages.error(request, 'Invalid Credentials. Please check.')
            


       # Check if a user with the same username already exists
        if User.objects.filter(username=usn).exists():
            messages.error(request, 'Account already exists. Please login to your account.')
            return render(request, 'loginPage.html')

        # If the user doesn't exist, create a new user
        user = User.objects.create_user(username=usn, password=passw, email=email)
        
        return render(request, 'home.html', {'username':usn,})
   
    # If the request method is not POST, render the registration page
    return render(request, 'loginPage.html'),messages('Wrong Credentials')

def redirectToLogin(request):
    return render(request,'loginPage.html')



def redirectToHome(request):
    return render(request,'loginPage.html',{})


def redirectToEwallet(request):
    return render(request,'Ewallet.html',{})


def redirectToTrackOne(request):
    return render(request,'Tracking.html',{})

def redirectToTrackTwo(request):
    return render(request,'TrackingTwo.html',{})





def redirectToEwalletViaLogin(request):
    if request.method == 'POST':
        usn = request.POST['username']
        passw = request.POST['password']

        User = auth.authenticate(username=usn, password=passw)
        if User is not None:
            auth.login(request, User)
            
            
            return render(request,'Ewallet.html',{})
        else:
            messages.error(request, 'Invalid Credentials. Please check.')
            return render(request,'loginPage.html')
    
    return render(request, 'loginPage.html',{'username':usn, })


def backToHome(request):
    usn=name.userName
    return render(request,'home.html',{'username':usn})
    
