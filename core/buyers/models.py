from django.db import models
from django.contrib.auth.models import User






class Byers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    from_signal = models.BooleanField(default=False)
    
    
    def __str__(self):
        return str(self.user.username)