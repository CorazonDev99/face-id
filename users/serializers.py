from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user_id', 'photo']

class RecognizeSerializer(serializers.Serializer):
    image = serializers.ImageField()
