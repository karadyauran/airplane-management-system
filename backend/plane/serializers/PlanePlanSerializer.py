from rest_framework import serializers
from ..models.PlanePlan import PlanePlan


class PlanePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanePlan
        fields = '__all__'

    def create(self, validated_data):
        return PlanePlan.objects.create(**validated_data)
