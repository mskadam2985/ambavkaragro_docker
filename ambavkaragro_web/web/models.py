from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank = True)

    def __str__(self):
        return self.name

class Brands(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True )

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    city = models.CharField(max_length=20, default='Mumbai')

    def __str__(self):
        return self.name