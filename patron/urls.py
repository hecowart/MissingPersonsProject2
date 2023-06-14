from django.urls import path
from .views import indexPageView, about,contact,post1,post2,post3,post4,current

urlpatterns = [
    path("", indexPageView, name="index"),
    path('about', about, name="about"),
    path('current/', current, name="current" ),
    path('contact/', contact, name="contact"),
    path('post1/', post1, name="post1"),
    path('post2/', post2, name="post2"),
    path('post3/', post3, name="post3"),
    path('post4/', post4, name="post4"),
]
