from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register(request):
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        contactemail = request.POST['contactemail']
        contactno = request.POST['contactno']
        password1 = request.POST['password1']
        user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,
                                        email=contactemail, password=password1)
        user.save()
        messages.info(request, "Patient has been registered successfully!")
        print("User created")
        return redirect('login')
    else:
        return render(request, "register.html")
    

def login(request):
    if request.method == 'POST' :
        print("User in login")
        username = request.POST['username']
        password = request.POST['password']

        user =  auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)    
        #    messages.info(request, "Patient has been login successfully!")
            return redirect('/')
        else :
           # messages.info(request, "Invalid credentials")
           messages.success(request, 'Patient  %s is not registered. Please register the patient first.' % username)
        
           return redirect('login')
    else:
         return render(request, "login.html")
    
def logout(request):
    auth.logout(request)
    return redirect('/')