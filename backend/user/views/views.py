from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status

from ..models.User import User

from django.shortcuts import get_object_or_404

from ..serializers.UserSerializer import UserSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_user_profile(request):
    return Response(request.user, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_users(request):
    planes = User.objects.all()
    serializer = UserSerializer(planes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def update_user(request):
    user = get_object_or_404(User, pk=request.user.id)
    data_for_update = request.data
    user.update(data_for_update)
    return Response(user.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def delete_user(request):
    user = get_object_or_404(User, pk=request.user.id)
    if user.is_valid():
        user.delete()
        return Response(status=status.HTTP_200_OK)

    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
