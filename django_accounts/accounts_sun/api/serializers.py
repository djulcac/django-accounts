from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
