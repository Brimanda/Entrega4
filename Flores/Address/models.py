from django.db import models
from Flower.models import User 

# Create your models here.

class ShippingAddress(models.Model):

    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    reference = models.CharField(max_length=200)
    zip = models.CharField(max_length=10, null=False, blank=False)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.zip
    
    def update_default(self, default=False):
        self.default = default 
        self.save()