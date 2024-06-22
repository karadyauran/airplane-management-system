from rest_framework import serializers
from ..models.Plane import Plane


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = '__all__'

    def create(self, validated_data):
        return Plane.objects.create(**validated_data)
