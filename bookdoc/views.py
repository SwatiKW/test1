from django.shortcuts import render
from .models import *
from datetime import date
from datetime import datetime
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def index(request):
    doctorList = doctor.objects.all()
    deptList = dept.objects.all()
    return render(request, "index.html", {'doctorList': doctorList, 'deptList': deptList})

def makeappointmentDoc(request):
   
    if request.method == 'POST' :
       
     #   print (request.POST) 

        #docname = request.POST['first_name']
        doctorList = doctor.objects.filter(id=int(request.POST['selectedDoctor'])).values('name')
        docname =""
        for doc in doctorList.all():
             docname = doc['name']

        

        apptime = str(request.POST['date'])
        appDate = apptime

        makeappointmentList = makeappointment.objects.filter(appDate=appDate, docname=docname).values()
        print(makeappointmentList)
        listLen  = len(makeappointmentList)
        if listLen > 0:
            messages.success(request, 'Please select another slot for doctor\'s booking!!')     
            return render(request, "index.html")


        patientname = request.POST['username']
        username = request.user.username
       #username = User.get_username()
        print(username)
        iswaiting = False
        emailid = request.POST['email']
        makeappointment_obj = makeappointment.objects.create(docname=docname, appDate=appDate, patientname=patientname, iswaiting=iswaiting, emailid=emailid, username = username)

        print("makeappointment_obj")

        messages.success(request, 'Congratulations %s! Your appointment has been booked successfully!!' % patientname)
        
        return render(request, "index.html")
    else:
          print("User in def makeappointmentDoc")
          print (request.GET) 
          username = request.GET['username']
          password = request.GET['password']
         

          return render(request, "appointment.html")





def showappointment(request):
   
    if request.method == 'POST' :
       
        print ("User in def showappointment") 

        appointmentList = makeappointment.objects.all()
        return render(request, "showappointment.html", {'appointmentList': appointmentList})
    else:
        print ("User in def showappointment") 

        appointmentList = makeappointment.objects.all()
        return render(request, "showappointment.html", {'appointmentList': appointmentList})



def search(request):
    #doctorList = doctor.objects.all()
    deptList = dept.objects.all()
    print (deptList)
    doctorList = doctor.objects.filter(dept='skin')
    return render(request, "search.html", {'doctorList': doctorList, 'deptList': deptList})

def cancelAppointment(request):
    #doctorList = doctor.objects.all()
    deptList = dept.objects.all()
    print (deptList)
    doctorList = doctor.objects.filter(dept='skin')
    return render(request, "search.html", {'doctorList': doctorList, 'deptList': deptList})

