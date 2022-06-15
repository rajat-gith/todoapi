from django.contrib import admin
from django.urls import path,include
from .views import TaskDetail, TaskList,TaskUpdate

urlpatterns = [
    path('',TaskList.as_view(),name='listcreate'),
    path('<int:pk>/', TaskDetail.as_view(), name='detailcreate'),
    path('<int:pk>/update',TaskUpdate.as_view(),name='updatetask')
] 

"""Basically in the first link the home page the 
api view will show only the list of todo items and it is
Used for read-write endpoints to represent a collection of model instances. """

"""In the second link the base_url/Specified todo item key
will show the details of the todo item and will allow the read,delete,update the
todo item
Used for read-write-delete endpoints to represent a single model instance."""

