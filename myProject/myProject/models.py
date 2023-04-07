from django.db import models
from django.contrib.auth.models import User


class textData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    textdata = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "posts"
        

class SubPost(models.Model):
    post = models.ForeignKey(textData, on_delete=models.CASCADE, related_name='subpost')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True)
    textdata = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "subpost"
        