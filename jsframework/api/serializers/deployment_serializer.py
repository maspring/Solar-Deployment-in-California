from rest_framework import serializers
from jsframework.models import Deployment, Statistics

class DeploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deployment

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics