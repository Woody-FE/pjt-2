from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()

class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
        )