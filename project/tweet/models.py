from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    text = models.TextField(max_length=500)
    photo =  models.ImageField(upload_to='photo/', blank=True, null=True)
    craeted_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:100]}'