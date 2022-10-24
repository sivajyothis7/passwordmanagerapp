from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entry(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    site_name = models.CharField(max_length=150)
    site_url = models.CharField(max_length=150,null=True)
    site_password = models.CharField(max_length=120)
    notes = models.CharField(max_length=100,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now_add=True)