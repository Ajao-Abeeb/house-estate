from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Property(models.Model):
     
    amentities_choice = (
        ('Balcony','Balcony'),
         ('Outdoor Kitchen','Outdoor Kitchen'),
         ('Cable Tv','Cable Tv'),
         ('Deck','Deck'),
         ('Two Parlour','Two Parlour'),
         ('Garden','Garden'),
         ('Tennis Courts','Tennis Courts'),
         ('Internet','Internet'),
         ('Parking','Parking'),
         ('Sun Room','Sun Room'),
         ('Swim House','Swim House'),
         ('Concrete Flooring','Concrete Flooring'),
         ('Tiles','Tiles'),
         
         
    )
    
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    interior_photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    price = models.IntegerField()
    property_id = models.IntegerField()
    location =models.CharField(max_length=255)
    property_type = models.CharField(max_length=255)
    status = models.CharField(max_length=10)
    area = models.CharField(max_length=30)
    bed = models.IntegerField()
    bath = models.IntegerField()
    garage = models.IntegerField()
    property_description = RichTextField()
    amentities = MultiSelectField(choices=amentities_choice, max_length=255)
    video = models.FileField(upload_to='video/%Y/%m/%d')
    floor_plan = models.ImageField(upload_to='photo/%Y/%m/%d')
    is_features = models.BooleanField (default= False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    
     
    
    def __str__(self):
        return self.title 
 

  