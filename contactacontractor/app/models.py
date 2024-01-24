from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    contractor = models.BooleanField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=100, default="available")
    is_completed = models.BooleanField()

class Quote(models.Model):
    contractor = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    accepted = models.BooleanField()


class Dispute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    reason = models.TextField(max_length=100)

