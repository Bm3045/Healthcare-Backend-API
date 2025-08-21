from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    # Password ko hash karne ke liye validation
    def validate_password(self, value: str) -> str:
        return make_password(value)

    # Extra validation: email unique ho
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists!")
        return value
