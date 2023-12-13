from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Endpoint
from .serializers import EndpointSerializer


# Create your views here.
class EndpointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows endpoints to be viewed or edited.
    """
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EndpointSerializer

    def get_queryset(self):
        return Endpoint.objects.filter(owner_id=self.request.user.id).order_by('-creation_date')

class Index(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        latest_endpoints_list = Endpoint.objects.filter(owner_id=request.user.id).order_by("-creation_date")
        context = {
            "latest_endpoints_list": latest_endpoints_list,
        }
        return render(request, "endpoints/index.html", context)