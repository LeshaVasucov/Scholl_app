from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE, related_name="creator")
    title = models.CharField(max_length=128)
    text = models.TextField()
    pict = models.ImageField(upload_to="picts/" ,blank=True)
    date = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.title}"