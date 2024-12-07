from django.db import models
from category.models import Category

# Create your models here.
class Place(models.Model):
    place_name   = models.CharField(max_length=200,unique=True)
    slug         =models.SlugField(max_length=200,unique=True)
    description  =models.TextField(max_length=500,blank=True)
    image        =models.ImageField(upload_to='photos/place',)
    category     =models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date =models.DateTimeField(auto_now_add=True)
    modified_date =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.place_name