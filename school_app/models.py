from django.db import models
from django.contrib.auth.models import User
# Create your models here.


MONTH_CHOICES = [('1', 'Вересень'),
                 ('2', 'Жовтень'),
                 ('3', 'Листопад'),
                 ('4', 'Грудень'),]

CATEGORY_CHOICES = [('0', 'Без категорії'),
                    ('1', 'Олімпіади'),
                    ('2', 'Конкурси'),
                    ('3', '--------'),]

class Post(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE, related_name="creator")
    title = models.CharField(max_length=128)
    text = models.TextField()
    pict = models.ImageField(upload_to="picts/" ,blank=True)
    date = models.DateField(null=True)
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES)
    month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    
    def __str__(self):
        return f"{self.title}"