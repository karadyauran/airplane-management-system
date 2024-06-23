from rest_framework import serializers
from ..models.Pilot import Pilot


class PilotSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Pilot
        fields = '__all__'

    def create(self, validated_data):
        pilot = Pilot.objects.create(**validated_data)
        pilot.save()

        return pilot
