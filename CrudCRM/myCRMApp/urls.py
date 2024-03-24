
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name="" ),
    
    path('register', views.register, name="register"),

    path('login', views.login, name="login"),

    #CRUD
    path('dashboard', views.dashboard, name="dashboard"),

    path('create_entry', views.create_entry, name="create_entry"),

    path('update_entry/<int:pk>', views.update_entry, name="update_entry"),

    path('record/<int:pk>', views.view_entry, name="record"),

    path('delete_entry/<int:pk>', views.delete_entry, name="delete_entry"),



    path('logout', views.logout, name="logout"),

]