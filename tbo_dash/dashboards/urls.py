from django.conf.urls import include, url
from tbo_dash.dashboards import views


urlpatterns = [

  url(r'^sensorvaluetype/(?P<id>[0-9]+)/$', views.SensorValueTypeAPIView.as_view()),
  url(r'^sensorvaluetype/$', views.SensorValueTypeAPIListView.as_view()),

  url(r'^sensor/(?P<id>[0-9]+)/$', views.SensorAPIView.as_view()),
  url(r'^sensor/$', views.SensorAPIListView.as_view()),

  url(r'^sensorvalue/(?P<id>[0-9]+)/$', views.SensorValueAPIView.as_view()),
  url(r'^sensorvalue/$', views.SensorValueAPIListView.as_view()),

  url(r'^device/(?P<id>[0-9]+)/$', views.DeviceAPIView.as_view()),
  url(r'^device/$', views.DeviceAPIListView.as_view()),

  url(r'^landfill/(?P<id>[0-9]+)/$', views.LandfillAPIView.as_view()),
  url(r'^landfill/$', views.LandfillAPIListView.as_view()),

  url(r'^dashboard/(?P<id>[0-9]+)/$', views.DashboardAPIView.as_view()),
  url(r'^dashboard/$', views.DashboardAPIListView.as_view()),

]
