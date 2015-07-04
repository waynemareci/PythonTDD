from django.conf.urls import include, url
from lists import views as list_views
from lists import urls as list_urls
from accounts import urls as account_urls
#from django.contrib import admin
#from lists import views

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^lists/',include(list_urls)),
    url(r'^accounts/',include(account_urls)),
#    url(r'^lists/new$',views.new_list,name='new_list'),
#    url('^lists/(\d+)/$',views.view_list,name='view_list'),
#    url('^lists/(\d+)/add_item$',views.add_item,name='add_item'),

    # url(r'^admin/', include(admin.site.urls)),
]
