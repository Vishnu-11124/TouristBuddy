from django.urls import path
from users import views

urlpatterns=[
    path('profile/update',views.EditProfile, name='edit-profile'),

]