from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    user_count = User.objects.count()
    print(user_count)
    return render(request, 'pyflame/index.html', {'user_count':user_count})