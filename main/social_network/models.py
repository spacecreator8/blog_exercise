from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    image = models.ImageField(upload_to='user_image')
    page = models.OneToOneField('Profile', on_delete=models.CASCADE, null=True)
    commentaries = models.ForeignKey('Message', on_delete=models.CASCADE, null=True, blank=True)




class Profile(models.Model):
    date_birth = models.DateField(blank=True, default=None, null=True)
    status = models.CharField(max_length=1000, blank=True, default='Привет я новенький :)')
    about = models.TextField(blank=True, default='Обо мне ...')


class Message(models.Model):
    page = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True, blank=True, default=None)
    text = models.TextField(max_length=1000, blank=True, default='')
    date = models.DateTimeField(auto_now=True)
