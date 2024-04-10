# from django.db import models

# # Create your models here.
# class Employee(models.Model):
#     name=models.CharField(max_length=50,null=True)
#     email=models.EmailField(max_length=70,null=True)
#     phone=models.IntegerField(null=True)


#     def __str__(self) :
#         return self.name 

# from statistics import mode
from django.db import models

# Create your models here.
class Employee(models.Model):
    usr_name=models.CharField(max_length=50,null=True)
    usr_email=models.EmailField(max_length=70,null=True)
    usr_phone=models.IntegerField(null=True)

    def __str__(self) :
        return self.usr_name
