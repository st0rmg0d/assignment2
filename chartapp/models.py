from django.db import models

# Create your models here.

class Product(models.Model):
    Address = models.CharField(max_length=100, null=False, blank=False)
    Balance = models.FloatField()

    def __str__(self):
        return f'{self.Address} - {self.Balance}'
        
