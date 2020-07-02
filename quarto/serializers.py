from rest_framework import serializers
from .models import User, Room

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RoomSerializer(serializers.Serializer):
    class Meta:
        model = Room
        fields = '__all__'
    