from django.db import models
#from django.contrib.auth.models import 
from django.contrib.auth import get_user_model

# Create your models here.

class ChatRoom(models.Model):
    name = models.CharField(max_length=50, unique=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


