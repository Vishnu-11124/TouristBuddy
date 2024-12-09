from django.contrib import admin
from .models import Place

# Register your models here.

class PlaceAdmin(admin.ModelAdmin):
    list_display =('place_name', 'category', 'modified_date', 'is_available')
    prepopulated_fields ={'slug':('place_name',)}
    
admin.site.register(Place,PlaceAdmin)