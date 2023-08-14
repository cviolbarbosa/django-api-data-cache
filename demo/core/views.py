from api_data_cache.mixins import  APIDataCacheListViewMixin
from rest_framework import serializers
from rest_framework import viewsets, mixins

from .models import MeasurementModel
# Create your views here.

class MeasurementPartialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementModel
        fields = ('id', 'name', 'start_at')


class MeasurementFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementModel
        fields = '__all__'


class ListRetrieveView(APIDataCacheListViewMixin,  mixins.RetrieveModelMixin,  viewsets.GenericViewSet):
    queryset = MeasurementModel.objects.all()
    search_fields = ['name', 'start_at']


    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'retrieve':
            return MeasurementFullSerializer
        if self.action == 'list' or self.action == 'advanced_list':
            return MeasurementPartialSerializer

