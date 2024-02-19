from django.conf import settings
from django.core import validators
from django.db import models
from django.dispatch import receiver

from algorithms.models import Algorithm

from algorithmServing.celery import debug_task

from endpoints.tasks import create_endpoint, delete_endpoint
from algorithmServing.celery import debug_task

class URIPathField(models.CharField):
    default_validators = [validators.RegexValidator("^\/([A-Za-z0-9]+((\/[A-Za-z0-9]+)?)+)$")]
    description = "A URI path component"

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 200
        super().__init__(*args, **kwargs)
    
    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if kwargs.get("max_length") == 200:
            del kwargs["max_length"]
        return name, path, args, kwargs


class Endpoint(models.Model):
    STATUS_CHOICES = {"creating": "creating", "active": "active", "terminating": "terminating"}
    
    name = models.CharField(max_length=255)
    creation_date = models.DateTimeField("date created")
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default="creating")
    path = URIPathField()
    algorithm = models.ForeignKey(Algorithm, default=None, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default='1', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


@receiver(models.signals.post_save, sender=Endpoint)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        create_endpoint.delay(instance.pk, instance.algorithm.pk)
        print(f"I was born!!! {instance.name}")

@receiver(models.signals.post_delete, sender=Endpoint)
def execute_after_delete(sender, instance, *args, **kwargs):
    delete_endpoint.delay(instance.name, instance.path, instance.algorithm.pk)
    print(f"I was murdered!!! {instance}")