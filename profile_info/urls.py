from django.urls import path
from profile_info import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
