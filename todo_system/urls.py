"""
URL configuration for todo_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from user_app.views import *
from task_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',Register.as_view(),name='signup'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',Logoutview.as_view(), name='logout'),
    path('task_add/',Add_task.as_view(), name='add_task'),
    path('',Tasklist.as_view(), name='home'),
    path('update_task/<int:pk>',TaskUpdate.as_view(), name='update_task'),
    path('delete_task/<int:pk>', Task_delete.as_view(), name= 'delete_task'),
    path('complete/<int:pk>', Task_complet.as_view(), name= "complete"),
    path('search/',TaskSearchView.as_view(),  name='search')

]
