from rest_framework import serializers
from .models import User, Role, UserRole, UserProfile

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8, max_length=128, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, min_length=8, max_length=128, style={'input_type': 'password'})
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

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description']

class UserRoleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    role = RoleSerializer()

    class Meta:
        model = UserRole
        fields = ['id', 'user', 'role']

    def create(self, validated_data):
        user = validated_data.pop('user')
        role = validated_data.pop('role')
        user_role = UserRole.objects.create(user=user, role=role)
        return user_role   

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'first_name', 'last_name', 'phone_number', 'address']

    def create(self, validated_data):
        user = validated_data.pop('user')
        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile