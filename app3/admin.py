# from django.contrib import admin
# from .models import Employee

# # Register your models here.


# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'phone']

# admin.site.register(Employee, EmployeeAdmin)

from django.contrib import admin
from .models import Employee
from app3.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['usr_name','usr_email','usr_phone']
admin.site.register(Employee,EmployeeAdmin)
    

