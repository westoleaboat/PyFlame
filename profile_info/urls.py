from django.urls import path
from profile_info import views

app_name = 'profile_info'

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
