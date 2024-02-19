from django.conf import settings
from django.db import models


class DeploymentNode(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateTimeField("date created")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default='1', on_delete=models.CASCADE)

    def __str__(self):
        return self.name