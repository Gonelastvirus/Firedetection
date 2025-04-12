# sensor_data/serializers.py
from rest_framework import serializers
from .models import SensorData
'''
class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['temperature', 'smoke', 'flame', 'humidity', 'timestamp','latitude','longitude']'''


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

