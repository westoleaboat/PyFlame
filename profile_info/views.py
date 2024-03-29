from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from django.http import HttpResponse, JsonResponse
from oauth2_provider.views import ProtectedResourceView
from oauth2_provider.views import ScopedProtectedResourceView

import json
from django.core.validators import validate_email
from oauth2_provider.views import ReadWriteScopedResourceView
from django.contrib.auth.decorators import login_required

from django_gravatar.helpers import get_gravatar_url, has_gravatar, get_gravatar_profile_url, calculate_gravatar_hash
# from django.contrib.auth.models import User
from django.contrib import messages
# from ..blog.models import Post


# Create your views here.

class ProfileView(LoginRequiredMixin, View):
    """ProfileView class accesses the user object via the request.
    This object is a built-in model defined and created by Django.
    Django automatically creates the user object and adds it to the
    request before the view is invoked. If the user is unauthenticated, ProfileView
    responds with a 401 status response. This status informs the client it is unauthorized to
    access profile information. If the user is authenticated, ProfileView responds with
    the user’s profile information."""

    def get(self, request):
        # object_list = Post.objects.filter(author=request.user).order_by('-created')
        # total_posts = object_list.count()

        return render(request, 'profile.html')#, {'total_posts':total_posts})


class EmailView(ProtectedResourceView):
    def get(self, request):
        return JsonResponse({'email': request.user.email, })


class ScopedEmailView(ScopedProtectedResourceView):
    required_scopes = ['email', ]

    def get(self, request):
        return JsonResponse({'email': request.user.email, })


class ReadWriteEmailView(ReadWriteScopedResourceView):
    required_scopes = ['email', ]

    def get(self, request):
        return JsonResponse({'email': request.user.email, })

    def patch(self, request):
        body = json.loads(request.body)
        email = body['email']
        validate_email(email)
        user = request.user
        user.email = email
        user.save(update_fields=['email'])
        return HttpResponse()
