from django.db import models
from django.contrib.auth.models import User
# Create your models here.


MONTH_CHOICES = [('1', 'Вересень'),
                 ('2', 'Жовтень'),
                 ('3', 'Листопад'),
                 ('4', 'Грудень'),]

class Post(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE, related_name="creator")
    title = models.CharField(max_length=128)
    text = models.TextField()
    pict = models.ImageField(upload_to="picts/" ,blank=True)
    date = models.DateField(null=True)
    month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    
    def __str__(self):
        return f"{self.title}"