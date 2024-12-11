from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from users.views import UserProfile, EditProfile

urlpatterns=[
    path('profile/update',views.EditProfile, name='edit-profile'),
        # User Authentication
    path('sign-up/', views.register, name="sign-in"),
    path('sign-in/', auth_views.LoginView.as_view(template_name="sign-up.html", redirect_authenticated_user=True), name='sign-up'),
    path('sign-out/', auth_views.LogoutView.as_view(template_name="sign-out.html"), name='sign-out'), 
]

