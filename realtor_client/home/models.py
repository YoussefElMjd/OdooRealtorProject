from django.db import models
from django.contrib.auth.models import AbstractUser 

class Client(AbstractUser):  
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email= models.EmailField(max_length=200)

    REQUIRED_FIELDS=['first_name', 'last_name', 'email'] 

    def save(self, *args, **kwargs):
          self.set_password(self.password)
          super().save(*args, **kwargs)


