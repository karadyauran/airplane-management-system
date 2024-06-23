from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from backend.pilot.models.Pilot import Pilot

from django.shortcuts import get_object_or_404

from backend.pilot.serializers.PilotSerializer import PilotSerializer


@api_view(['GET'])
def get_pilot(request, pk):
    pilot = get_object_or_404(Pilot, pk=pk)
    serializer = PilotSerializer(pilot)

    if serializer.is_valid():
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_pilots(request):
    pilots = Pilot.objects.all()
    serializer = PilotSerializer(pilots, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_pilot(request, pk):
    pilot = get_object_or_404(Pilot, pk=pk)
    serializer = PilotSerializer(pilot, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_pilot(request, pk):
    pilot = get_object_or_404(Pilot, pk=pk)
    pilot.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
