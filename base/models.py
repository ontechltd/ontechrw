from django.db import models

# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=100, null=False, blank=False)
    class_name = models.CharField(max_length=100, null=False, blank=False)
    service_desc = models.TextField(null=False, blank=False)
    service_image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.service_name
    
    
