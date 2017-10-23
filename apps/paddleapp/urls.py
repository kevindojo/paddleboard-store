from django.conf.urls import url,include
from . import views           
urlpatterns = [
  url(r'^$', views.index),
  url(r'^buy$', views.buy),
  url(r'^login$', views.login),
  url(r'^create$', views.create),
  url(r'^result$', views.result)
#   url(r'^add$', views.add),  
#   url(r'^clear$', views.clear)
  
]