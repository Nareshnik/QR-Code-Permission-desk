from django.contrib import admin
from home.models import Permissions, Student, Faculty

# Register your models here.
admin.site.register(Permissions) 
admin.site.register(Students) 
admin.site.register(Faculty)
