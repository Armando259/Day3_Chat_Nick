from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from datetime import date  # Import the date module

class Korisnik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    
    def __str__(self):
        return self.user.email

class Event(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    
    name = models.CharField(max_length=255)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    affected_brand = models.CharField(max_length=255)
    description = models.TextField(max_length=1500)
    malicious_url = models.URLField()
    malicious_domain_registration_date = models.DateField(default=date.today)  # Set default to today's date
    malicious_domain_dns_a = models.CharField(max_length=255)
    malicious_domain_dns_ns = models.CharField(max_length=255)
    malicious_domain_dns_mx = models.CharField(max_length=255)
    matching_keywords = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
