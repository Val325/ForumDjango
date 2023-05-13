from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, to_field='username', unique=True)
    avatar = models.ImageField(upload_to='images/', blank=True, null=True)
    class Meta:
        db_table = "profile"
        


class textData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    time = models.DateTimeField(auto_now_add=True)
    textdata = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.CharField(max_length=200, default='', blank=True, null=True)
    class Meta:
        db_table = "posts"
        

class SubPost(models.Model):
    post = models.ForeignKey(textData, on_delete=models.CASCADE, related_name='subpost')
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    textdata = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default='', blank=True, null=True)
    class Meta:
        db_table = "subpost"
        