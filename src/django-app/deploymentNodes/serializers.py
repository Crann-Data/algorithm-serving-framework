from rest_framework import serializers

from .models import DeploymentNode


class DeploymentNodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeploymentNode
        fields = "__all__"
    