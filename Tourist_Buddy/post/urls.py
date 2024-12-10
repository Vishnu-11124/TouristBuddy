from django.urls import path
from post import views

urlpatterns=[
    path('',views.post, name='post'),
    path('newpost/', views.NewPost, name='newpost'),
    path('tag/<slug:tag_slug>', views.Tags, name='tags'),
    path('<uuid:post_id>/like', views.like, name='like'),
    #path('<uuid:post_id>/', views.PostDetail, name='postdetails')
]