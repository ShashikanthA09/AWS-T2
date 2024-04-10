from django.db import models

# Create your models here.
class user (models.Model):
    usr_name=models.CharField(max_length=50,null=True)
    usr_email=models.EmailField(max_length=70,null=True)
    usr_phone=models.IntegerField(null=True)

    def __str__(self) :
        return self.usr_name


# class Employee (models.Model):
#     emp_name=models.CharField(max_length=50,null=True)
#     emp_name=models.CharField(max_length=50,null=True)
#     emp_name=models.CharField(max_length=50,null=True)
#     emp_name=models.CharField(max_length=50,null=True)
#     emp_name=models.CharField(max_length=50,null=True)
#     emp_name=models.CharField(max_length=50,null=True)
#     emp_email=models.EmailField(max_length=70,null=True)
#     emp_phone=models.IntegerField(null=True)

#     # def __str__(self) :
#     #     return self.emp_name        