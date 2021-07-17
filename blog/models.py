from django.db import models
from django.utils import timezone

# Create your models here.


class blog(models.Model):
    tophead = models.TextField(max_length=100)
    Date = models.DateTimeField(default=timezone.now)
    blogimage = models.ImageField(upload_to='images/')
    blogtext = models.TextField(max_length=200)
