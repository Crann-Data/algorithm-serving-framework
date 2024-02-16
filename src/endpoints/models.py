from django.conf import settings
from django.core import validators
from django.db import models
from django.dispatch import receiver

from algorithms.models import Algorithm


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

# Create your models here.
class Endpoint(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateTimeField("date created")
    path = URIPathField()
    algorithm = models.ForeignKey(Algorithm, default=None, on_delete=models.SET_DEFAULT)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default='1', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


@receiver(models.signals.post_save, sender=Endpoint)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        print(f"I was born!!! {instance}")

@receiver(models.signals.post_delete, sender=Endpoint)
def execute_after_delete(sender, instance, *args, **kwargs):
    print(f"I was murdered!!! {instance}")