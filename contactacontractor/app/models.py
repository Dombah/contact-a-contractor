from django.db import models

from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    contractor = models.BooleanField()
    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name}"
    
class Job(models.Model):

    JOB_STATUS_AVAILABLE = "available"
    JOB_STATUS_ACCEPTED = "accepted"
    JOB_STATUS_IN_PROGRESS = "in progress"
    JOB_STATUS_COMPLETE = "complete"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=100, default=JOB_STATUS_AVAILABLE)
    is_completed = models.BooleanField()
    def __str__(self):
        return f"{self.user.account.first_name} {self.user.account.last_name} - {self.title}"

class Quote(models.Model):
    contractor = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    accepted = models.BooleanField()
    def __str__(self):
        return f"{self.contractor.username} - {self.job}: {self.price}"

class Dispute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    reason = models.TextField(max_length=100)
    def __str__(self):
        return f"Dispute for: {self.job}"

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    text = models.TextField()
    def __str__(self):
        return f"{self.sender} to {self.receiver} - {self.text}"
    
class Rating(models.Model):
    rater = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rater")
    ratee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratee")
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    review = models.TextField(max_length=100, default="")
    rating = models.IntegerField()
    def __str__(self):
        return f"{self.job.title} - Rating: {self.rating}"