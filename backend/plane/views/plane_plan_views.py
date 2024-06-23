from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models.Plane import Plane

from django.shortcuts import get_object_or_404

from ..serializers.PlanePlanSerializer import PlanePlanSerializer


@api_view(['GET'])
def get_plane_plan(request, pk):
    plan = get_object_or_404(Plane, pk=pk)
    serializer = PlanePlanSerializer(plan)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_plane(request):
    data = request.data
    plane_plan = PlanePlanSerializer(data=data)
    if plane_plan.is_valid():
        plane_plan.create(validated_data=data)
        return Response(plane_plan.data, status=status.HTTP_201_CREATED)

    return Response(plane_plan.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_plane(request, pk):
    data = request.data
    plane_plan = get_object_or_404(Plane, pk=pk)
    plane_plan.update(data)
    return Response(plane_plan.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_plane(request, pk):
    plane_plan = get_object_or_404(Plane, pk=pk)
    if plane_plan.is_valid():
        plane_plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_400_BAD_REQUEST)
