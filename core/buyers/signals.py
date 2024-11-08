from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Byers






@receiver(post_save, sender=User)
def post_save_create_buyer(sender, instance, created, **kwargs):
    print('sender: ', sender)
    print('instance: ', instance)
    print('created: ', created)
    if created:
        Byers.objects.get_or_create(user=instance)