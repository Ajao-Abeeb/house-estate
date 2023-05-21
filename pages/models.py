from django.db import models
from ckeditor.fields import RichTextField
# from datetime import datetime

# Create your models here.

class Testimony(models.Model):
    image = models.ImageField(upload_to='photo/%Y/%m/%d')
    text =  RichTextField()
    name = models.CharField(max_length=100)
    image_small = models.ImageField(upload_to='photo/%Y/%m/%d')
    

    def __str__(self):
        return self.name

    
   
