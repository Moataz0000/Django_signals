from django.db import models
from buyers.models import Byers
import uuid


class Car(models.Model):
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    buyer = models.ForeignKey(Byers, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, blank=True)
    
    
    def __str__(self):
        return str(self.name)
    
    # def save(self, *args, **kwargs):
    #     if not self.code:
    #         self.code = str(uuid.uuid4()).replace('-','').upper()[:10]
    #     return super().save(*args, **kwargs)