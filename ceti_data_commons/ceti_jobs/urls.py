from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import CreateView

urlpatterns = [
    path('jobs', views.create_job, name='jobs'),
    path('create_job/', CreateView.as_view(), name="create_job"),

]

urlpatterns = format_suffix_patterns(urlpatterns)