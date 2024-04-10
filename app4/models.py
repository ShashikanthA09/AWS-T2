from django.db import models

# Create your models here.
class Data(models.Model):
    company_name = models.CharField(max_length=100)
    software_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.company_name