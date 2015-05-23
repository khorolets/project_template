from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'profit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace="accounts", app_name="accounts")),
    url(r'^transactions/', include('transactions.urls', namespace="transactions", app_name="transactions")),
]

# rest api

urlpatterns += [
    url(r'^api/transactions/', include('transactions.api.urls', namespace="api_transactions", app_name="transactions")),
]
