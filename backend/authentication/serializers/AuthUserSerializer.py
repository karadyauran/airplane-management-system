from rest_framework import serializers
from ..models.AuthUser import AuthUser


class AuthUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta(object):
        model = AuthUser
        fields = '__all__'

    def create(self, validated_data):
        user = AuthUser.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
