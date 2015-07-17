from django.conf.urls import url
from jsframework.api.views.deployment_view import DeploymentView, StatisticsView


urlpatterns = [
    # check as_view for bugs.
    url(r'^$', StatisticsView.as_view()),
    url(r'^$', DeploymentView.as_view())
]