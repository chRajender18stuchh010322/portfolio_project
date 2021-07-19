from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.


class Job(models.Model):
    header = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="images/")
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.header
