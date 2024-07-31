from django.db import models

# Create your models here.

class Contact_us(models.Model):
    name=models.CharField(max_length=100, null=True)
    email=models.EmailField(max_length=100, null=True)
    phone=models.CharField(max_length=30, null=True)
    subject=models.CharField(max_length=100, null=True)
    message=models.TextField()
    def __str__(self):
        return self.name

