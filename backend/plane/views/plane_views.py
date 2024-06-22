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
