from rest_framework import serializers
from ..models.User import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)

        return user
