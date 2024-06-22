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
