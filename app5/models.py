from django.db import models

# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name

# class user1 (models.Model):
#     usr1_name=models.CharField(max_length=50,null=True)
#     usr1_email=models.EmailField(max_length=70,null=True)
#     usr1_phone=models.IntegerField(null=True)

#     def __str__(self) :
#         return self.usr1_name        