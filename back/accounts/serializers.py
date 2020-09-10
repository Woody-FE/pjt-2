from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()

class CreateUserSerializer(serializers.ModelSerializer):
    child_name = serializers.CharField(required=False)
    child_gender = serializers.CharField(required=False)
    child_image = serializers.ImageField(required=False)
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'child_name',
            'child_gender',
            'child_image',
        )