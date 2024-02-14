from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_rooms, name='chat_rooms'),
    path('create-room/', views.create_room, name='create_room'),
    path('room/<str:room_name>/', views.room_detail, name='room_detail'),
]
