from django.conf.urls import url
from .views import ValList, ValDetail, ValCreate, ValUpdate, ValDelete

urlpatterns = [
    url(r'^$', ValList.as_view(), name='val-list'), #values list
    #url(r'^values/(?P<pk>[0-9]+)/$', ValDetail.as_view(), name='val-detail'),
    url(r'values/add/$', ValCreate.as_view(), name='val-add'),
    url(r'values/(?P<pk>[0-9]+)/$', ValUpdate.as_view(), name='val-update'),
    url(r'values/(?P<pk>[0-9]+)/delete/$', ValDelete.as_view(), name='val-delete'),
]
