from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    is_organizer = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.jpg')


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', default='default.png')

    def __str__(self):
        return self.user.username

class Document(models.Model):
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    organizer = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    event_image = models.ImageField(upload_to='event_images/', default='event_images/default.jpg')
    pdf = models.FileField(upload_to='event_pdfs/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Register(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    register_date = models.DateTimeField(auto_now_add=True)




