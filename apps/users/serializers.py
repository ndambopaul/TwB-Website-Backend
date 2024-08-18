from rest_framework import serializers
from apps.users.models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"