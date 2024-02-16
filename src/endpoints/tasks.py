from celery import shared_task
from time import sleep

@shared_task
def create_endpoint(name, path, algorithm):
    return name, path, algorithm

@shared_task
def delete_endpoint(name, path, algorithm):
    return name, path, algorithm