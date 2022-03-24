from django.db import models

# Create your models here.

class router_details(models.Model):
    Sapid = models.AutoField(primary_key=True)
    Hostname = models.CharField(max_length=200)
    Loopback = models.GenericIPAddressField()
    Mac_address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Hostname