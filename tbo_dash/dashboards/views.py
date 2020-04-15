from rest_framework.viewsets import ModelViewSet
from tbo_dash.dashboards.serializers import (
    SensorValueTypeSerializer, SensorSerializer, SensorValueSerializer,
    DeviceSerializer, LandfillSerializer, DashboardSerializer)
from tbo_dash.dashboards.models import (
    SensorValueType, Sensor, SensorValue, Device, Landfill, Dashboard)


class SensorValueTypeViewSet(ModelViewSet):
    queryset = SensorValueType.objects.order_by('pk')
    serializer_class = SensorValueTypeSerializer


class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.order_by('pk')
    serializer_class = SensorSerializer


class SensorValueViewSet(ModelViewSet):
    queryset = SensorValue.objects.order_by('pk')
    serializer_class = SensorValueSerializer


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.order_by('pk')
    serializer_class = DeviceSerializer


class LandfillViewSet(ModelViewSet):
    queryset = Landfill.objects.order_by('pk')
    serializer_class = LandfillSerializer


class DashboardViewSet(ModelViewSet):
    queryset = Dashboard.objects.order_by('pk')
    serializer_class = DashboardSerializer
