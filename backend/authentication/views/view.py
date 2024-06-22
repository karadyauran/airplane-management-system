from ..models.AuthUser import AuthUser
from ..serializers.AuthUserSerializer import AuthUserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def signup(request):
    """ Sign up for new user. """
    serializer = AuthUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.create(request.data)
        token, created = Token.objects.get_or_create(user=user)

        serialized_user = AuthUserSerializer(user).data

        return Response({"token": token.key, "user": serialized_user}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    """ Login for new user. """
    auth_user = get_object_or_404(AuthUser, username=request.data['email'])
    if not auth_user.check_password(request.data['password']):
        return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=auth_user)
    serialized_user = AuthUserSerializer(auth_user).data

    return Response({"token": token.key, "user": serialized_user}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def logout(request):
    """ Log out user from session """
    try:
        request.user.auth_token.delete()

        return Response({'detail': f'Successfully logged out for {request.user.email}.'}, status=status.HTTP_200_OK)
    except (AttributeError, Token.DoesNotExist):
        return Response({'detail': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
