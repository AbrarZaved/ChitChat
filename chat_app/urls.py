from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chat_room/<slug:slug>", views.chat_room, name="chat_room"),
    path("create_room", views.create_room, name="create_room"),
    path("delete_room/<slug:slug>", views.delete_room, name="delete_room"),
]
