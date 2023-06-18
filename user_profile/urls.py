from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_user,name = 'login'),
    path('logout/',logout_user,name = 'logout'),
    path('profile/',profile,name = 'profile'),
    path('register/',register_user,name = 'register'),
    path('change_profile_picture/',change_profile_picture,name = 'change_profile_picture'),
    path('profilechange/',profilechange,name = 'profilechange'),
    path('change_password/',change_password,name = 'change_password'),
    
    
    # path('forgot_password/',forgot_password,name = 'forgot_password'),  
    # path('forgot_password_done/',forgot_password_done,name = 'forgot_password_done'),    
      
    
    
    
    
]