from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models.User import User

from django.shortcuts import get_object_or_404

from ..serializers.UserSerializer import UserSerializer


@api_view(['GET'])
def get_user(request):
    user = get_object_or_404(User, pk=request.GET.get('pk'))
    serialized_data = UserSerializer(user)
    return Response(serialized_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_users(request):
    planes = User.objects.all()
    serializer = UserSerializer(planes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    data = request.data
    user.update(data)
    return Response(user.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.is_valid():
        user.delete()
        return Response(status=status.HTTP_200_OK)

    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
