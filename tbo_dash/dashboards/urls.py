from rest_framework.routers import SimpleRouter
from tbo_dash.dashboards import views


router = SimpleRouter()

router.register(r'sensorvaluetypes', views.SensorValueTypeViewSet)
router.register(r'sensors', views.SensorViewSet)
router.register(r'sensorvalues', views.SensorValueViewSet)
router.register(r'devices', views.DeviceViewSet)
router.register(r'landfills', views.LandfillViewSet)
router.register(r'dashboards', views.DashboardViewSet)

urlpatterns = router.urls
