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

# Create your views here.


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):

        return render(request, 'profile.html')


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
