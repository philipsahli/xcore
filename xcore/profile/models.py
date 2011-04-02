from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # General
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    url = models.URLField()
    user = models.ForeignKey(User, unique=True, editable=False)
    
    class Meta:
        db_table = 'xcore_userprofile'
