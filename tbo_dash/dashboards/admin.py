from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import (Dashboard, Device, Landfill, Sensor,
                     SensorValue, SensorValueType)


@admin.register(Dashboard)
class DashboardAdmin(ImportExportActionModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    filter_horizontal = ("landfills", 'users')


@admin.register(Device)
class DeviceAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'fw_ver', 'landfill')
    list_filter = ('fw_ver', 'landfill')
    search_fields = ('name',)


@admin.register(Landfill)
class LandfillAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'organization')
    list_filter = ('organization',)
    search_fields = ('name',)


@admin.register(Sensor)
class SensorAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'device', 'value_type')
    list_filter = ('device', 'value_type')
    search_fields = ('name',)


@admin.register(SensorValue)
class SensorValueAdmin(ImportExportActionModelAdmin):
    list_display = ('sensor', 'value', 'timestamp')
    list_filter = ('sensor',)


@admin.register(SensorValueType)
class SensorValueTypeAdmin(ImportExportActionModelAdmin):
    pass
