from django.contrib import admin
from django.urls import path
from ChlorineWaterApi import views

urlpatterns = [
   
    
    path('', views.login_user, name='login'),
    # #path('post-todo', views.post_todo, name='todo'),
    # #path('post-login', views.post_login, name='todo'),
    path('UserRegistration', views.user_register, name='register'),
    path('UserLogin', views.UserLogin, name='todo'),
    path('Get_State_List', views.Get_state, name='get_state'),
    path('Get_City_List', views.Get_City_List, name='get_state'),
    path('Get_Site_Status', views.Get_Site_Status, name='sitestatus'),
    path('Get_Command_List', views.Get_Command_List, name='commandlist'),
    path('Get_Device_Status', views.Get_Device_Status, name='devicestatus'),
    path('getStatusPanel', views.getstatusPanel, name='getStatusPanel'),
    path('getSiteMap', views.showMap, name='getSiteMap'),
    path('getSiteDevice', views.getSiteDevice, name='getSitedevice'),
    path('updateDeviceSetting', views.updateDeviceSetting, name='updateDeviceSetting')
    
    

]



#superuser credantial is  admin and admin