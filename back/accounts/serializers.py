from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework import serializers

from rest_auth.models import TokenModel
from rest_auth.utils import import_callable
from allauth.account import app_settings as allauth_settings
from allauth.utils import (email_address_exists,
                            get_username_max_length)
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.base import AuthProcess

from .models import Family


User = get_user_model()


class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'child_name',
            'child_gender',
        )


class FamilyDetailSerializer(serializers.ModelSerializer):
    user = UserUpdateSerializer()
    class Meta:
        model = Family
        fields = (
            'id',
            'user',
            'name',
            'image',
            'gender'
        )


class UserDetailSerializer(UserUpdateSerializer):
    username = serializers.CharField(required=False)
    class Meta:
        model = User
        depth = 1
        fields = UserUpdateSerializer.Meta.fields + ('child_image', 'families')


class UserChildImageUpdateSerializer(UserUpdateSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'child_image',
        )


class UserFamilySerializer(serializers.ModelSerializer):
    class Meat:
        model = User
        fields = (
            'families'
        )


class FamilyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = (
            'name',
            'image',
            'gender',
        )


class FamilyBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        depth = 1
        fields = (
            'id',
            'name',
            'image',
            'gender',
        )


class FamilyUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)
    gender = serializers.CharField(required=False)
    class Meta:
        model = Family
        fields = (
            'name',
            'image',
            'gender',
        )


class CustomTokenSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = TokenModel
        fields = (
            'key',
            'user',
        )


class RegisterSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    def validate_email(self, email):
        return email

    def validate_password(self, password):
        return password

    def get_cleaned_data(self):
        return {
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', '')
        }

    def save(self, request):
        user = get_user_model()
        cleaned_data = self.get_cleaned_data()
        user.create_user(**cleaned_data)
        return user


class RegisterSerializer(serializers.Serializer):
    child_name = serializers.CharField(
        required=True
    )
    email = serializers.EmailField(required=settings.ACCOUNT_EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_childname(self, child_name):
        child_name = get_adapter().clean_username(child_name)
        return child_name

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and email_address_exists(email):
            raise serializers.ValidationError(
                "A user is already registered with this e-mail address.")
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'child_name': self.validated_data.get('child_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.child_name = request.data.get('child_name')
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])

        return user