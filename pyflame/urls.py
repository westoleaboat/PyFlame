"""https://django-registration.readthedocs.io/en/latest/quickstart.html"""

from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),

]
