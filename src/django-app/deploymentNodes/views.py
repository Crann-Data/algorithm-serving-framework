from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import DeploymentNode
from .serializers import DeploymentNodeSerializer

# Create your views here.
class DeploymentNodeViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DeploymentNodeSerializer

    def get_queryset(self):
        return DeploymentNode.objects.filter(owner_id=self.request.user.id).order_by('-creation_date')

class Index(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        deployment_node_list = DeploymentNode.objects.filter(owner_id=request.user.id).order_by("-creation_date")
        context = {
            "deployment_node_list": deployment_node_list,
        }
        return render(request, "deploymentNodes/index.html", context)