from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    url(r'^demo/$', views.DemoView.as_view(), name='demo'),
]
