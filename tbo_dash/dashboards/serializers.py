from rest_framework.serializers import ModelSerializer
from tbo_dash.dashboards.models import (
    SensorValueType, Sensor, SensorValue, Device, Landfill, Dashboard)


class SensorValueTypeSerializer(ModelSerializer):

    class Meta:
        model = SensorValueType
        depth = 3
        fields = '__all__'


class SensorSerializer(ModelSerializer):

    class Meta:
        model = Sensor
        depth = 3
        fields = '__all__'


class SensorValueSerializer(ModelSerializer):

    class Meta:
        model = SensorValue
        depth = 3
        fields = '__all__'


class DeviceSerializer(ModelSerializer):

    class Meta:
        model = Device
        depth = 3
        fields = '__all__'


class LandfillSerializer(ModelSerializer):

    class Meta:
        model = Landfill
        depth = 3
        fields = '__all__'


class DashboardSerializer(ModelSerializer):

    class Meta:
        model = Dashboard
        depth = 3
        fields = '__all__'
