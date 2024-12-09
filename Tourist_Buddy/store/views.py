from django.shortcuts import render,get_object_or_404
from .models import Place
from category.models import  Category
# Create your views here.

def store(request, category_slug=None):
    categories=None
    places =None
    if category_slug != None:
        categories= get_object_or_404(Category, slug=category_slug)
        places= Place.objects.all().filter(category=categories, is_available=True)
    else:
        places= Place.objects.all().filter(is_available=True)
    
    context= {
        'places':places,
    }
    
    return render(request, 'store/store.html',context)

def place_detail(request,category_slug,place_slug):
    try:
        single_place = Place.objects.get(category__slug=category_slug,slug=place_slug)
    except Exception as e:
        raise e
    
    context={
        'single_place': single_place,
    }
    return render(request, 'store/place_detail.html',context)