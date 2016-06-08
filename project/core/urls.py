from django.conf.urls import include, url
from django.contrib import admin
from django.views.debug import default_urlconf

urlpatterns = [
    # Examples:
    url(r'^$', default_urlconf),
    # url(r'^$', 'profit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

# rest api
#
#urlpatterns += [    
#]
