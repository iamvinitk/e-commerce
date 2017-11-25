from django.conf.urls import url
from django.contrib.auth import views as auth_views

from user import views

urlpatterns = [
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'kompany:home'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^remove_item/(?P<product_id>[-\w]+)/$', views.remove_item_from_cart, name='remove_item'),
    # url(r'^add_item/(?P<product_id>[-\w]+)/$', views.add_item, name='add_item'),
    url(r'^add_item/$', views.add_item, name='add_item'),
    url(r'^add_address/$', views.add_address, name='add_address'),
    url(r'^checkout/$', views.check_out, name='check_out'),
    url(r'^checkout/(?P<product_id>[-\w]+)/$', views.check_out_item, name='check_out_item'),
    url(r'^order_placed/$', views.order_placed, name='order_placed')
]