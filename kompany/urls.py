from django.conf.urls import url
from kompany import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^search/$', views.search, name='search'),
    url(r'^product/(?P<product_id>[-\w]+)/$', views.product_page, name='product_page'),
    url(r'^(?P<category>[a-z]+)/(?P<page_index>[-\w]+)/$', views.category_view, name='product_list'),
    url(r'^(?P<category>[-\w]+)/$', views.category_view, name='product_list'),
]
