from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=200)
    doctor_id = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=200)
    
