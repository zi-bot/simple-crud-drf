from django.db import models

# Create your models here.

class UserProfile(models.Model):
    lname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)