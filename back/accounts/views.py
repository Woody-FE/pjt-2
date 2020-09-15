from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from .serializers import UserUpdateSerializer, UserDetailSerializer, UserChildImageUpdateSerializer


User = get_user_model()


class UserDetailView(APIView):
    
    permission_classes = (IsAuthenticated,)

    def get_object(self, user_id):
        return get_object_or_404(User, pk=user_id)

    @swagger_auto_schema()
    def get(self, request, user_id):
        user = self.get_object(user_id)
        serializer = UserDetailSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, user_id):
        if request.user.id == user_id:
            user = self.get_object(user_id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)

    @swagger_auto_schema(request_body=UserDetailSerializer)
    def patch(self, request, user_id):
        if request.user.id == user_id:
            user = self.get_object(user_id)
            serializer = UserUpdateSerializer(instance=user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)


class UserImageUpdateView(APIView):

    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser, )

    @swagger_auto_schema(request_body=UserChildImageUpdateSerializer)
    def patch(self, request, user_id):
        if request.user.id == user_id:
            user = get_object_or_404(User, pk=user_id)
            serializer = UserChildImageUpdateSerializer(instance=user, data=request.FILES)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(UserDetailSerializer(instance=user).data ,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)