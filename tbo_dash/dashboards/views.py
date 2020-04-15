from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from tbo_dash.dashboards.serializers import SensorValueTypeSerializer, SensorSerializer, SensorValueSerializer, DeviceSerializer, LandfillSerializer, DashboardSerializer
from tbo_dash.dashboards.models import SensorValueType, Sensor, SensorValue, Device, Landfill, Dashboard


class SensorValueTypeAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = SensorValueType.objects.get(pk=id)
            serializer = SensorValueTypeSerializer(item)
            return Response(serializer.data)
        except SensorValueType.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = SensorValueType.objects.get(pk=id)
        except SensorValueType.DoesNotExist:
            return Response(status=404)
        serializer = SensorValueTypeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = SensorValueType.objects.get(pk=id)
        except SensorValueType.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SensorValueTypeAPIListView(APIView):

    def get(self, request, format=None):
        items = SensorValueType.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = SensorValueTypeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SensorValueTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SensorAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Sensor.objects.get(pk=id)
            serializer = SensorSerializer(item)
            return Response(serializer.data)
        except Sensor.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Sensor.objects.get(pk=id)
        except Sensor.DoesNotExist:
            return Response(status=404)
        serializer = SensorSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Sensor.objects.get(pk=id)
        except Sensor.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SensorAPIListView(APIView):

    def get(self, request, format=None):
        items = Sensor.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = SensorSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SensorValueAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = SensorValue.objects.get(pk=id)
            serializer = SensorValueSerializer(item)
            return Response(serializer.data)
        except SensorValue.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = SensorValue.objects.get(pk=id)
        except SensorValue.DoesNotExist:
            return Response(status=404)
        serializer = SensorValueSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = SensorValue.objects.get(pk=id)
        except SensorValue.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SensorValueAPIListView(APIView):

    def get(self, request, format=None):
        items = SensorValue.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = SensorValueSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SensorValueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DeviceAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Device.objects.get(pk=id)
            serializer = DeviceSerializer(item)
            return Response(serializer.data)
        except Device.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Device.objects.get(pk=id)
        except Device.DoesNotExist:
            return Response(status=404)
        serializer = DeviceSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Device.objects.get(pk=id)
        except Device.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DeviceAPIListView(APIView):

    def get(self, request, format=None):
        items = Device.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DeviceSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class LandfillAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Landfill.objects.get(pk=id)
            serializer = LandfillSerializer(item)
            return Response(serializer.data)
        except Landfill.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Landfill.objects.get(pk=id)
        except Landfill.DoesNotExist:
            return Response(status=404)
        serializer = LandfillSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Landfill.objects.get(pk=id)
        except Landfill.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class LandfillAPIListView(APIView):

    def get(self, request, format=None):
        items = Landfill.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = LandfillSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = LandfillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DashboardAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Dashboard.objects.get(pk=id)
            serializer = DashboardSerializer(item)
            return Response(serializer.data)
        except Dashboard.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Dashboard.objects.get(pk=id)
        except Dashboard.DoesNotExist:
            return Response(status=404)
        serializer = DashboardSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Dashboard.objects.get(pk=id)
        except Dashboard.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DashboardAPIListView(APIView):

    def get(self, request, format=None):
        items = Dashboard.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DashboardSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DashboardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
