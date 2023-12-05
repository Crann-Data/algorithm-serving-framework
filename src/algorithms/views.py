from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, FileResponse
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.core.files import File
from django.utils import timezone
from PIL import Image

from .models import Algorithm


# Create your views here.

def index(request):
    latest_algorithms_list = Algorithm.objects.order_by("-creation_date")[:5]
    context = {
        "latest_algorithms_list": latest_algorithms_list,
    }
    return render(request, "algorithms/index.html", context)

def get_algo_details(request, algorithm_id):
    try:
        algo = Algorithm.objects.get(pk=algorithm_id)
    except Algorithm.DoesNotExist:
        raise Http404("Algorithm does not exist")
    file = open(algo.algorithm_file.path, mode="rb")
    return FileResponse(file, as_attachment=True, filename=algo.algorithm_file.name)

def upload_algorithm(request):
    if request.method == "POST":
        file = File(request.FILES["file"])
        new_algo = Algorithm(name=file.name, creation_date=timezone.now(), algorithm_file=file)
        new_algo.save()
        return HttpResponseRedirect("/")
    else:
        return HttpResponseBadRequest()