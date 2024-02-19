from django.conf import settings
from django.db import models
from .validators import validate_file_extension

# Create your models here.
class Algorithm(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateTimeField("date created")
    algorithm_file = models.FileField(upload_to="algorithm_storage", validators=[validate_file_extension])
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default='1', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
