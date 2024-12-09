
from django.urls import path
from . import views


urlpatterns = [
    path('',views.store,name='store'),
    path('<slug:category_slug>/',views.store,name='places_by_category'),
    path('<slug:category_slug>/<slug:place_slug>/',views.place_detail,name='place_detail'),
] 
