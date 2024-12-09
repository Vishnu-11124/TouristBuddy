from django.shortcuts import render
from store.models import Place

def home(request):
    places= Place.objects.all().filter(is_available=True)

    context= {
        'places':places,
    }
    return render(request,'home.html',context)