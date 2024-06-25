from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status

from ..models.Plane import Plane

from django.shortcuts import get_object_or_404

from ..serializers.PlanePlanSerializer import PlanePlanSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_plane_plan(request, pk):
    plan = get_object_or_404(Plane, pk=pk)
    serializer = PlanePlanSerializer(plan)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_plane(request):
    if request.user.user.role.value == 'SUD':
        data = request.data
        plane_plan = PlanePlanSerializer(data=data)
        if plane_plan.is_valid():
            plane_plan.create(validated_data=data)
            return Response(plane_plan.data, status=status.HTTP_201_CREATED)

        return Response(plane_plan.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def update_plane(request, pk):
    if request.user.user.role.value == 'SUD':
        data = request.data
        plane_plan = get_object_or_404(Plane, pk=pk)
        plane_plan.update(data)
        return Response(plane_plan.data, status=status.HTTP_200_OK)
    return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def delete_plane(request, pk):
    if request.user.user.role.value == 'SUD':
        plane_plan = get_object_or_404(Plane, pk=pk)
        if plane_plan.is_valid():
            plane_plan.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
