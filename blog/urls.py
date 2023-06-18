from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name = 'home'),
    path('video/',video,name = 'video'),
    path('category_video/<str:slug>/', category_blog,name = 'categoryvideo'),
    path('video/<str:slug>/',blog_details,name = 'blogdetails'),
    path('add_reply/<int:blog_id>/<int:comment_id>/',add_reply,name = 'add_reply'), 
    path('scoreboard/', scoreboard, name = 'scoreboard'),
    
    
]