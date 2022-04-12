import profile
from django.urls import path
from .views import *


urlpatterns = [
    path('',index, name = "home"),
    
    path('category/<str:choice>/',index ),
    path('register/', register, name = "register"),
    path('login/',loginPage,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('createprofile/',createProfile,name = 'create'),
    path('updateprofile/',updateProfile,name = 'update'),
    path('recommended/', recommended, name='recommended'),
    path('profile/',profile,name = 'profile'),

]
