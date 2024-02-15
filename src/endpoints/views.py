from django.shortcuts import render
from django.utils import timezone

from rest_framework import status, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Endpoint
from algorithms.models import Algorithm
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
        algorithms_list = Algorithm.objects.filter(owner_id=request.user.id).order_by("-creation_date")
        context = {
            "algorithms_list": algorithms_list,
            "latest_endpoints_list": latest_endpoints_list,
        }
        return render(request, "endpoints/index.html", context)
    
class CreateEndpoint(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        
        serialized_endpoint = EndpointSerializer(data={"name": request.data['name'], 
                                                       "creation_date":timezone.now(), 
                                                       "path": request.data['path'], 
                                                       "algorithm": request.data['algorithm'],
                                                       "owner": request.user.id})
        if serialized_endpoint.is_valid():
            serialized_endpoint.save()
            return Response({"data": f"file submitted: {serialized_endpoint.data}"},status=status.HTTP_201_CREATED)
        return Response({"data": f"bad file request: {serialized_endpoint.errors}"}, status=status.HTTP_400_BAD_REQUEST)
    