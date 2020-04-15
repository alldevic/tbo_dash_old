from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import (Dashboard, Device, Landfill, Sensor,
                     SensorValue, SensorValueType)


@admin.register(Dashboard)
class DashboardAdmin(ImportExportActionModelAdmin):
    pass


@admin.register(Device)
class DeviceAdmin(ImportExportActionModelAdmin):
    pass


@admin.register(Landfill)
class LandfillAdmin(ImportExportActionModelAdmin):
    pass


@admin.register(Sensor)
class SensorAdmin(ImportExportActionModelAdmin):
    pass


@admin.register(SensorValue)
class SensorValueAdmin(ImportExportActionModelAdmin):
    pass


@admin.register(SensorValueType)
class SensorValueTypeAdmin(ImportExportActionModelAdmin):
    pass
