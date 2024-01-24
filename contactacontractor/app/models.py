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