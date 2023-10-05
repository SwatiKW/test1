from django.db import models

# Create your models here.

class doctor(models.Model):
    name = models.CharField(max_length= 100)
    speciality = models.TextField()
    idphoto = models.ImageField(upload_to='pics')
    desc = models.TextField()
    emailid = models.EmailField()
    dept = models.TextField(default='')


class dept(models.Model):
    dept = models.TextField(default='')

class makeappointment(models.Model):
    docname = models.CharField(max_length= 100)
    appDate = models.CharField(max_length= 100)
    emailid = models.EmailField(default=0)
    patientname = models.CharField(max_length= 100)
    username = models.CharField(max_length= 100)
    iswaiting = models.BooleanField(default=False)
 