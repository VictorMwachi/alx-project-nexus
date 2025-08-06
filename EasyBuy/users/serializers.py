from rest_framework import serializers
from .models import User, Role, UserRole

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8, max_length=128, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, min_length=8, max_length=128, style={'input_type': 'password'})
    email = serializers.EmailField(required=True, max_length=255, allow_blank=False)
    class Meta:
        model = User
        fields = ['email', 'password','password2']
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user