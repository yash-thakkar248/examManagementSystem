from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)
    user_type = serializers.ChoiceField(choices=(('student', 'Student'), ('instructor', 'Instructor')))

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user_type = data.get('user_type')

        if not username or not password or not user_type:
            raise serializers.ValidationError("All fields are required")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Incorrect username or password")

        # Check if the authenticated user has the correct user_type
        if user.user_type != user_type:
            raise serializers.ValidationError("User type does not match")

        data['user'] = user
        return data