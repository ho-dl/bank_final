from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def demo(request):
    return render(request,"index.html")



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            # Check if a user with the same username or email already exists
            if User.objects.filter(username=username).exists():
                error_message = "Username already exists. Please choose a different username."
            elif User.objects.filter(email=email).exists():
                error_message = "Email already exists. Please use a different email."
            else:
                # Create the user if the username and email are unique
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                print("User created")
                return redirect('login')
        else:
            error_message = "Passwords do not match."

        return render(request, "register.html", {'error_message': error_message})

    return render(request, "register.html")

def contact(request):
    return render(request,"contact.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            error_message = "invalid credential."

        return render(request, "login.html", {'error_message': error_message})

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def submit_form(request):
    if request.method == 'POST':

        return render(request, 'contact.html', {'success_message': 'Application Accepted!'})

    return render(request, 'contact.html')