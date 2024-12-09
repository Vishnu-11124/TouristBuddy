from django.db import models
from store.models import Place

# Create your models here.

class Wishlist(models.Model):
    wishlist_id = models.CharField(max_length=250,blank=True)
    date_added =models.DateField(auto_now_add=True)

    def __str__(self):
        return self.wishlist_id
    
class WishlistItem(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    Wishlist =models.ForeignKey(Wishlist,on_delete=models.CASCADE)
    quantity =models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.place