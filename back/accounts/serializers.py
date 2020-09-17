from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'child_name',
            'child_gender',
        )


class UserDetailSerializer(UserUpdateSerializer):
    class Meta:
        model = User
        fields = UserUpdateSerializer.Meta.fields + ('child_image',)


class UserChildImageUpdateSerializer(UserUpdateSerializer):
    class Meta:
        model = User
        fields = (
            'child_image',
        )