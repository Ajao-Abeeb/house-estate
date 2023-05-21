from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Agent(models.Model):
    image = models.ImageField(upload_to='photo/%Y/%m/%d')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    about = models.TextField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=30)
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    linkedin_link = models.URLField(max_length=100)
    skype = models.CharField(max_length=20)
    is_features = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
