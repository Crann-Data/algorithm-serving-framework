from celery import shared_task
from endpoints.models import Endpoint
from algorithms.models import Algorithm

from celery import Celery
app = Celery()

def create_endpoint(endpoint_pk, algorithm_pk):
    endpoint = Endpoint.objects.get(pk=endpoint_pk)
    algorithm = Algorithm.objects.get(pk=algorithm_pk)
    return endpoint_pk, algorithm_pk

@shared_task
def delete_endpoint(endpoint_pk, algorithm_pk):
    return endpoint_pk, algorithm_pk
