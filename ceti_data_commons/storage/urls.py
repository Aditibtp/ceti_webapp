from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^storage_id/$', CreateView.as_view(), name="create_storage_id"),
    url(r'^get-token/', obtain_auth_token), # Add this line
}

urlpatterns = format_suffix_patterns(urlpatterns)