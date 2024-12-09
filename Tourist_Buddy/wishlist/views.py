

from django.shortcuts import render,redirect
from store.models import Place
from .models import Wishlist,WishlistItem
from django.http import HttpResponse

# Create your views here.

def _wishlist_id(request):
    wishlist =request.session.session_key
    if not wishlist:
        wishlist =request.session.create()
    return wishlist

def add_wishlist(request,place_id):
    place = Place.objects.get(id=place_id)
    try:
        wishlist =Wishlist.objects.get(wishlist_id=_wishlist_id(request))
    except Wishlist.DoesNotExist:
        wishlist=Wishlist.objects.create(
            wishlist_id =_wishlist_id(request)
        )
    wishlist.save()

    try:
        wishlist_item = WishlistItem.objects.get(place=place,wishlist=wishlist)
        wishlist_item.quantity += 1
        wishlist_item.save()
    except WishlistItem.DoesNotExist:
        wishlist_item=WishlistItem.objects.create(
            place =place,
            quantity = 1,
            wishlist=wishlist,
        )
        wishlist_item.save() 
    return HttpResponse(wishlist_item.place)
    exit()    
    return redirect('wishlist')   


def wishlist(request):
    return render(request,'store/wishlist.html')