from django.conf.urls import include, url
from django.contrib import admin
from django.views.debug import default_urlconf

urlpatterns = [
    url(r'^$', default_urlconf),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
]

# rest api

urlpatterns += [
    url(r'^api/v0/', include('api.v0.common.urls', namespace='api_v0')),
]
