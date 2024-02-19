from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def index(request):
    if not request.user.is_anonymous:
        return render(request, "home/index.html")
    else:
        return HttpResponseRedirect("accounts/login/")