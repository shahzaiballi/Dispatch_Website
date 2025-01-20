# core/models.py
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class SignUp(models.Model):
    TRUCK_TYPES = [
        ('box', 'Box Truck'),
        ('flatbed', 'Flatbed'),
        ('reefer', 'Reefer'),
        ('van', 'Van'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    truck_type = models.CharField(max_length=20, choices=TRUCK_TYPES)
    trailer_size = models.CharField(max_length=50)
    mc_copy = models.FileField(upload_to='documents/mc/')
    noa = models.FileField(upload_to='documents/noa/')
    insurance_cert = models.FileField(upload_to='documents/insurance/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.truck_type}"