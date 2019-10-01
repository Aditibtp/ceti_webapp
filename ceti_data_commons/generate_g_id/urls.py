from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CreateView

from .views import DetailsView

urlpatterns = {
    url(r'^storage_id/$', CreateView.as_view(), name="get_storage_id"),

}

urlpatterns = format_suffix_patterns(urlpatterns)