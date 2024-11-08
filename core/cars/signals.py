from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Car
import uuid
from buyers.models import Byers

# work before the model saved.

@receiver(pre_save, sender=Car)
def pre_save_create(sender, instance, **kwargs):
    if not instance.code:
        instance.code = str(uuid.uuid4()).replace('-','').upper()[:10] 
        
    obj = Byers.objects.get(user=instance.buyer.user)
    obj.from_signal = True
    obj.save()