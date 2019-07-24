from django.conf.urls import url
from .views import *



urlpatterns = [
    url(r'^login/$', login, name="insert_user"),

    url(r'^user/set/insert/$', UserDetailCreateAPIView.as_view(), name="insert_user"),
    url(r'^user/set/update/(?P<pk>[0-9]+)/$', UserDetailUpdateAPIView.as_view(), name="update_user"),
    url(r'^user/set/delete/(?P<pk>[0-9]+)/$', UserDetailUpdateAPIView.as_view(), name="delete_user"),
    url(r'^user/set/active/(?P<pk>[0-9]+)/$', UserDetailActiveAPIView.as_view(), name="active_user"),
    url(r'^user/get/select/$', UserAllAPIView.as_view(), name="select_user"),
    url(r'^user/get/select/(?P<pk>[0-9]+)/$', UserDetailUpdateAPIView.as_view(), name="selectpk_user"),
    url(r'^user/get/select/process/(?P<pk>[0-9]+)/$', UserSelectProcess.as_view(), name="selectpk_user"),

    url(r'^usertype/set/insert/$', UserTypeCreateAPIView.as_view(), name="insert_usertype"),
    url(r'^usertype/set/update/(?P<pk>[0-9]+)/$', UserTypeUpdateAPIView.as_view(), name="update_usertype"),
    url(r'^usertype/set/delete/(?P<pk>[0-9]+)/$', UserTypeUpdateAPIView.as_view(), name="delete_usertype"),
    url(r'^usertype/set/active/(?P<pk>[0-9]+)/$', UserTypeUpdateAPIView.as_view(), name="active_usertype"),
    url(r'^usertype/get/select/$', UserTypeCreateAPIView.as_view(), name="select_usertype"),
    url(r'^usertype/get/select/(?P<pk>[0-9]+)/$', UserTypeUpdateAPIView.as_view(), name="selectpk_usertype"),

]