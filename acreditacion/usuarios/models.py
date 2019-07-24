from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# Create your models here.

class UserDetail(models.Model):
    id_user = models.CharField(unique=True,max_length=10,blank=True,null=True)
    id_usertype = models.CharField(max_length=10,blank=True,null=True)
    photo = models.CharField(max_length=50,blank=True,null=True)
    status = models.CharField(max_length=1,blank=True,null=True, default="1")
    created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True) 

class UserType(models.Model):
    name = models.CharField(unique=True, max_length=25)
    status = models.CharField(max_length=1, blank=True, null=True, default="1")
    created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True) 

# Documentos
#Procesos

# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)