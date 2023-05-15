from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.
class Agent(models.Model):
    image = models.ImageField(upload_to='photo/%Y/%m/%d')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    about = RichTextField()
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=30)
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    linkedin_link = models.URLField(max_length=100)
    is_features = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name

class Testimony(models.Model):
    image = models.ImageField(upload_to='photo/%Y/%m/%d')
    text =  RichTextField()
    name = models.CharField(max_length=100)
    image_small = models.ImageField(upload_to='photo/%Y/%m/%d')
    

    def __str__(self):
        return self.name

    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photo/%Y/%m/%d')
    author = models.CharField(max_length=255)
    date =  models.DateTimeField(datetime.now().strftime('%d %b %Y'))
    header = RichTextField()
    description = RichTextField()
    quote = models.CharField(max_length=255)
    quote_author = models.CharField(max_length=255)
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    linkedin_link = models.URLField(max_length=100)
    is_features = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

     
