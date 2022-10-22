from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),


]



# to restart the redis server:
# ---------------------------
# 1.wsl
# 2.sudo service redis-server start
# 3.sudo service redis-server status
# i need to go and login to the admin
# gagana,Gowri@123