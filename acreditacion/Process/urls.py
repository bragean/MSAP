from django.conf.urls import url
from .views import *
from . import views
from django.urls import path



urlpatterns = [
    url(r'^document/set/insert/$', DocumentCreateAPIView.as_view(), name="insert_document"),
    url(r'^document/set/update/(?P<pk>[0-9]+)/$', DocumentUpdateAPIView.as_view(), name="update_document"),
    url(r'^document/set/delete/(?P<pk>[0-9]+)/$', DocumentUpdateAPIView.as_view(), name="delete_document"),
    url(r'^document/set/active/(?P<pk>[0-9]+)/$', DocumentActiveAPIView.as_view(), name="active_document"),
    url(r'^document/get/select/$', DocumentCreateAPIView.as_view(), name="select_document"),
    url(r'^document/get/select/(?P<pk>[0-9]+)/$', DocumentUpdateAPIView.as_view(), name="selectpk_document"),

    url(r'^process/set/insert/$', ProcessCreateAPIView.as_view(), name="insert_process"),
    url(r'^process/set/update/(?P<pk>[0-9]+)/$', ProcessUpdateAPIView.as_view(), name="update_process"),
    url(r'^process/set/delete/(?P<pk>[0-9]+)/$', ProcessUpdateAPIView.as_view(), name="delete_process"),
    url(r'^process/set/active/(?P<pk>[0-9]+)/$', ProcessActiveAPIView.as_view(), name="active_process"),
    url(r'^process/get/select/$', ProcessSelect.as_view(), name="select_process"),
    url(r'^process/get/select/(?P<pk>[0-9]+)/$', ProcessUpdateAPIView.as_view(), name="selectpk_process"),
    url(r'^process/get/calculate/$', ProcessCalculate.as_view(), name="phase_calculate"),
    url(r'^process/get/select/user/(?P<pk>[0-9]+)/$', ProcessSelectUser.as_view(), name="select_user"),


    url(r'^phase/set/insert/$', PhaseCreateAPIView.as_view(), name="insert_phase"),
    url(r'^phase/set/update/(?P<pk>[0-9]+)/$', PhaseUpdateAPIView.as_view(), name="update_phase"),
    url(r'^phase/set/delete/(?P<pk>[0-9]+)/$', PhaseUpdateAPIView.as_view(), name="delete_phase"),
    url(r'^phase/set/active/(?P<pk>[0-9]+)/$', PhaseActiveAPIView.as_view(), name="active_phase"),
    url(r'^phase/get/select/$', PhaseCreateAPIView.as_view(), name="select_phase"),
    url(r'^phase/get/select/(?P<pk>[0-9]+)/$', PhaseUpdateAPIView.as_view(), name="selectpk_phase"),
    url(r'^phase/get/select/process/(?P<pk>[0-9]+)/$', PhaseSelectProcess.as_view(), name="selectpk_phase"),
    url(r'^phase/get/calculate/(?P<pk>[0-9]+)/$', PhaseCalculate.as_view(), name="phase_calculate"),

    url(r'^criteria/set/insert/$', CriteriaCreateAPIView.as_view(), name="insert_criteria"),
    url(r'^criteria/set/update/(?P<pk>[0-9]+)/$', CriteriaUpdateAPIView.as_view(), name="update_criteria"),
    url(r'^criteria/set/delete/(?P<pk>[0-9]+)/$', CriteriaUpdateAPIView.as_view(), name="delete_criteria"),
    url(r'^criteria/set/active/(?P<pk>[0-9]+)/$', CriteriaActiveAPIView.as_view(), name="active_criteria"),
    url(r'^criteria/get/select/$', CriteriaCreateAPIView.as_view(), name="select_criteria"),
    url(r'^criteria/get/select/(?P<pk>[0-9]+)/$', CriteriaUpdateAPIView.as_view(), name="selectpk_criteria"),
    url(r'^criteria/get/select/process/(?P<pk>[0-9]+)/$', CriteriaSelectProcess.as_view(), name="selectpk_phase"),
    url(r'^criteria/get/calculate/(?P<pk>[0-9]+)/(?P<pk2>[0-9]+)/$', CriteriaCalculate.as_view(), name="selectpk_phase"),

    url(r'^indicator/set/insert/$', IndicatorCreateAPIView.as_view(), name="insert_indicator"),
    url(r'^indicator/set/update/(?P<pk>[0-9]+)/$', IndicatorUpdateAPIView.as_view(), name="update_indicator"),
    url(r'^indicator/set/delete/(?P<pk>[0-9]+)/$', IndicatorUpdateAPIView.as_view(), name="delete_indicator"),
    url(r'^indicator/set/active/(?P<pk>[0-9]+)/$', IndicatorActiveAPIView.as_view(), name="active_indicator"),
    url(r'^indicator/get/select/$', IndicatorCreateAPIView.as_view(), name="select_indicator"),
    url(r'^indicator/get/select/(?P<pk>[0-9]+)/$', IndicatorUpdateAPIView.as_view(), name="selectpk_indicator"),
    url(r'^indicator/get/select/criteria/(?P<pk>[0-9]+)/$', IndicatorSelectCriteria.as_view(), name="selectpk_phase"),
    url(r'^indicator/get/select/process/(?P<pk>[0-9]+)/$', IndicatorSelectProcess.as_view(), name="selectpk_phase"),
    url(r'^indicator/get/calculate/(?P<pk>[0-9]+)/(?P<pk2>[0-9]+)/$', IndicatorCalculate.as_view(), name="selectpk_phase"),

    url(r'^task/set/insert/$', TaskCreateAPIView.as_view(), name="insert_task"),
    url(r'^task/set/update/(?P<pk>[0-9]+)/$', TaskUpdateAPIView.as_view(), name="update_task"),
    url(r'^task/set/delete/(?P<pk>[0-9]+)/$', TaskUpdateAPIView.as_view(), name="delete_task"),
    url(r'^task/set/active/(?P<pk>[0-9]+)/$', TaskActiveAPIView.as_view(), name="active_task"),
    url(r'^task/get/select/$', TaskCreateAPIView.as_view(), name="select_task"),
    url(r'^task/get/select/(?P<pk>[0-9]+)/$', TaskUpdateAPIView.as_view(), name="selectpk_task"),
    url(r'^task/get/select/indicator/(?P<pk>[0-9]+)/$', TaskSelectIndicator.as_view(), name="selectpk_phase"),
    url(r'^task/get/select/phase/(?P<pk>[0-9]+)/$', TaskSelectPhase.as_view(), name="selectpk_phase"),
    url(r'^task/set/status/(?P<pk>[0-9]+)/$', TaskChangeStatus.as_view(), name="status_task"),
    url(r'^task/get/calculate/(?P<pk>[0-9]+)/$', TaskCount.as_view(), name="selectpk_phase"),

    url(r'^upload', FileUploadView.as_view(), name="upload"),
    url(r'^notification', Notification.as_view(), name="notification"),
    url(r'^report/', views.create_report, name='report'),
    
]