from django.contrib.auth.models import User
from django.core.files import File
from django.http import (FileResponse, Http404, HttpResponse,
                         HttpResponseBadRequest, HttpResponseRedirect)
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Algorithm
from .serializers import AlgorithmSerializer

# Create your views here.

class AlgorithmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows algorithms to be viewed or edited.
    """
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AlgorithmSerializer

    def get_queryset(self):
        print(self.request.user)
        return Algorithm.objects.filter(owner_id=self.request.user.id).order_by('-creation_date')

class Index(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        latest_algorithms_list = Algorithm.objects.filter(owner_id=request.user.id).order_by("-creation_date")
        context = {
            "latest_algorithms_list": latest_algorithms_list,
        }
        return render(request, "algorithms/index.html", context)
    

class AlgoDetails(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, algorithm_id, format=None):
        try:
            algo = Algorithm.objects.get(pk=algorithm_id)
        except Algorithm.DoesNotExist:
            return HttpResponse("algorithm does not exist", status=status.HTTP_404_NOT_FOUND)
    
        if not algo.owner.id == request.user.id:
            return HttpResponse("unauthorised", status=status.HTTP_401_UNAUTHORIZED)
        serial = AlgorithmSerializer(algo)
        return Response(serial.data)


class UploadAlgorithm(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        if not "file" in request.FILES:
            return Response({"data": "No file given"}, status=status.HTTP_400_BAD_REQUEST)
        file = File(request.FILES["file"])
        serialized_algo = AlgorithmSerializer(data={"name": file.name, "creation_date":timezone.now(), "algorithm_file":file, "owner": request.user.id})
        if serialized_algo.is_valid():
            serialized_algo.save()
            return Response({"data": f"file submitted: {serialized_algo.data}"},status=status.HTTP_201_CREATED)
        return Response({"data": f"bad file request: {serialized_algo.errors}"}, status=status.HTTP_400_BAD_REQUEST)
    
class DownloadAlgorithm(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, algorithm_id, format=None):
        try:
            algo = Algorithm.objects.get(pk=algorithm_id)
        except Algorithm.DoesNotExist:
            return HttpResponse("algorithm does not exist", status=status.HTTP_404_NOT_FOUND)
    
        if not algo.owner.id == request.user.id:
            return HttpResponse("unauthorised", status=status.HTTP_401_UNAUTHORIZED)
        file = open(algo.algorithm_file.path, mode="rb")
        return FileResponse(file, as_attachment=True, filename=algo.algorithm_file.name)