from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, FileResponse
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.core.files import File
from django.utils import timezone

from rest_framework import  viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import User

from .models import Algorithm
from .serializers import AlgorithmSerializer


# Create your views here.

class AlgorithmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows algorithms to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = AlgorithmSerializer

    def get_queryset(self):
        return Algorithm.objects.filter(owner_id=self.request.user.id).order_by('-creation_date')


def index(request):
    latest_algorithms_list = Algorithm.objects.filter(owner_id=request.user.id).order_by("-creation_date")
    context = {
        "latest_algorithms_list": latest_algorithms_list,
    }
    return render(request, "algorithms/index.html", context)

def get_algo_details(request, algorithm_id):
    try:
        algo = Algorithm.objects.get(pk=algorithm_id)
    except Algorithm.DoesNotExist:
        return HttpResponse("algorithm does not exist", status=status.HTTP_404_NOT_FOUND)
    
    if not algo.owner.id == request.user.id:
        return HttpResponse("unauthorised", status=status.HTTP_401_UNAUTHORIZED)
    file = open(algo.algorithm_file.path, mode="rb")
    return FileResponse(file, as_attachment=True, filename=algo.algorithm_file.name)

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def upload_algorithm(request):
    if request.method == "POST":
        if not "file" in request.FILES:
            return Response({"data": "No file given"}, status=status.HTTP_400_BAD_REQUEST)
        file = File(request.FILES["file"])
        serialized_algo = AlgorithmSerializer(data={"name": file.name, "creation_date":timezone.now(), "algorithm_file":file, "owner": User.objects.get(id=request.user.id)})
        if serialized_algo.is_valid():
            serialized_algo.save()
            return Response({"data": f"file submitted: {serialized_algo.data}"},status=status.HTTP_201_CREATED)
        return Response({"data": f"bad file request: {serialized_algo.errors}"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"data": ""}, status=status.HTTP_405_METHOD_NOT_ALLOWED)