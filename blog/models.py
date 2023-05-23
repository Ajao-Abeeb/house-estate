from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photo/%Y/%m/%d')
    author = models.CharField(max_length=255)
    date =  models.DateTimeField(default=datetime.now())
    header = RichTextField()
    description = RichTextField()
    quote = models.CharField(max_length=255)
    quote_author = models.CharField(max_length=255)
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    linkedin_link = models.URLField(max_length=100)
    is_features = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length= 200)
    comment = models.TextField(max_length= 1000)
    email = models.TextField(max_length=20)
    date = models.DateTimeField(default=datetime.now())
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
     
    
    
    def __str__(self):
        return self.comment

  