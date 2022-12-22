from django.db import models

class OdooUser(models.Model):  
    url = models.CharField(max_length=256)
    db = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)


