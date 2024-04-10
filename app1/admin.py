from django.contrib import admin
from app1.models import user
# from app1.models import Employee

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['usr_name','usr_email','usr_phone']
admin.site.register(user,UserAdmin)

# class EmployeeAdmin(admin.ModelAdmin):
#     list_display=['usr_name','usr_email','usr_phone']
# admin.site.register(Employee,EmployeeAdmin)