from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^buy$', views.buy),
    url(r'^registration$', views.registration),
    url(r'^result$', views.result),
    url(r'^users$', views.display),
    url(r'^users/new$', views.new, name='my_new'),
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit, name='my_edit'),
    url(r'^users/(?P<user_id>\d+)$', views.show, name='my_show'),
    url(r'^users/create$', views.create, name='my_create'),
    url(r'^users/(?P<user_id>\d+)/destroy$', views.destroy, name='my_delete'),
    url(r'^users/(?P<user_id>\d+)/update$', views.update, name='my_update'),
    #   url(r'^add$', views.add),
    #   url(r'^clear$', views.clear)

]
