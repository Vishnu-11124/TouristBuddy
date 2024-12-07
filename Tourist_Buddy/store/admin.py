from django.contrib import admin
from .models import Place

# Register your models here.

class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('place_name',)}
    list_display =('place_name', 'category', 'modified_date')
    

admin.site.register(Place,PlaceAdmin)