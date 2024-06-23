from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models.Plane import Plane

from django.shortcuts import get_object_or_404

from ..serializers.PlaneSerializer import PlaneSerializer


@api_view(['GET'])
def get_plans(request):
    plane = get_object_or_404(Plane, pk=request.GET.get('pk'))
    serializer = PlaneSerializer(plane)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_plane(request):
    data = request.data
    plane = PlaneSerializer(data)
    if plane.is_valid():
        plane.create(data)

        return Response(plane.data, status=status.HTTP_201_CREATED)

    return Response(plane.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_plane(request, pk):
    plane = get_object_or_404(Plane, pk=pk)

    data = request.data
    plane.update(data)
    return Response(plane.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_plane(request, pk):
    plane = get_object_or_404(Plane, pk=pk)
    plane.delete()
    return Response(status=status.HTTP_200_OK)
