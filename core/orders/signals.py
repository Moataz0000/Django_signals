from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from .models import Order
from sales.models import Sale




@receiver(m2m_changed, sender=Order.cars.through)
def m2m_change_cars_orders(sender, instance, action, **kwargs):
    print(action)
    total = 0
    total_price = 0
    
    for car in instance.cars.all():
        total += 1
        total_price  += car.price
    instance.total = total
    instance.total_price = total_price
    instance.save()
    
    

@receiver(post_save, sender=Order)
def post_save_create_or_update_sale(sender, instance, created, **kwargs):
       obj, _ = Sale.objects.get_or_create(order=instance)
       obj.amount = instance.total_price
       obj.save()