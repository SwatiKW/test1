from django.contrib import admin
from .models import doctor, dept, makeappointment

# Register your models here.

admin.site.register(doctor)
admin.site.register(dept)
admin.site.register(makeappointment)