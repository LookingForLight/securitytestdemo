from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'comment/', views.comment, name='comment'),
    re_path(r'showlist/', views.showlist, name='showlist'),
    re_path(r'test/', views.test, name='test'),
    re_path(r'result/$', views.result, name='test')
]