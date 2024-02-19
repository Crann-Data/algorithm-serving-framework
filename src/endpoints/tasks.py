from celery import shared_task
# from algorithms.models import Algorithm
# from endpoints.models import Endpoint

@shared_task
def create_endpoint(endpoint_pk, algorithm_pk):


    return endpoint_pk, algorithm_pk

@shared_task
def delete_endpoint(name, path, algorithm_pk):
    return name, path, algorithm_pk