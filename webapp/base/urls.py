from django.conf.urls import url
from django.contrib import admin

from credits import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index_view'),
    url(r'^select-customer/$', views.select_customer, name='select_customer'),
    url(r'^customer-data/$', views.show_customer_data, name='show_customer_data'),
]
