from django.contrib import admin
# from app5.models import user

# Register your models here.
from .models import *

admin.site.register(Employees)


# class UserAdmin1(admin.ModelAdmin):
#     list_display=['usr1_name','usr1_email','usr1_phone']
# admin.site.register(user,UserAdmin1)