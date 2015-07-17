from rest_framework.generics import ListCreateAPIView
from jsframework.api.serializers.deployment_serializer import DeploymentSerializer, StatisticsSerializer
from jsframework.models import Deployment, Statistics
from django.db.models import Avg
# import django_filters -- May need to import this module later to use the Djangofilter function Alex suggested


class DeploymentView(ListCreateAPIView):
    serializer_class = DeploymentSerializer
    queryset = Deployment.objects.all()
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('city', 'zipcode')

    def get_queryset(self):
        return Deployment.objects.all()[:100]
        # return Deployment.objects.all().filter(cost__lte=12000).filter(cost__gte=10000)[:100]


class StatisticsView(ListCreateAPIView):
    serializer_class = StatisticsSerializer
    queryset = Statistics.objects.all()

    def get_queryset(self):
        return Statistics.objects.all()


