from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from .models import Family
from .image_to_cartoon.make_hat_and_face_image import show_me_hat_and_face
from .serializers import UserUpdateSerializer, UserDetailSerializer, UserChildImageUpdateSerializer, FamilyCreateSerializer, FamilyDetailSerializer, FamilyBasicSerializer, FamilyUpdateSerializer


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
        user = self.get_object(user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(request_body=UserDetailSerializer)
    def patch(self, request, user_id):
        user = self.get_object(user_id)
        serializer = UserUpdateSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class UserImageUpdateView(APIView):

    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser, )

    def get_object(self, user_id):
        return get_object_or_404(User, pk=user_id)

    @swagger_auto_schema(request_body=UserChildImageUpdateSerializer)
    def patch(self, request, user_id):
        user = self.get_object(user_id)
        serializer = UserChildImageUpdateSerializer(instance=user, data=request.FILES)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(UserDetailSerializer(instance=user).data ,status=status.HTTP_200_OK)
    
    def delete(self, request, user_id):
        user = self.get_object(user_id)
        user.child_image.delete(save=True)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserFamilyView(APIView):

    permission_classes = (IsAuthenticated, )
    parser_classes = (FormParser, MultiPartParser, )

    def get_user(self, user_id):
        return get_object_or_404(User, pk=user_id)

    @swagger_auto_schema()
    def get(self, request, user_id):
        user = self.get_user(user_id)
        serializer = FamilyBasicSerializer(instance=user.families, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=FamilyCreateSerializer)
    def post(self, request, user_id):
        user = self.get_user(user_id)
        serializer = FamilyCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserFamilyDetailView(APIView):

    permission_classes = (IsAuthenticated, )
    parser_classes = (FormParser, MultiPartParser, )

    def get_family(self, family_id):
        return get_object_or_404(Family, pk=family_id)
    
    def check_userid(self, family, user_id):
        if family.user.id == user_id:
            return True
        return False

    @swagger_auto_schema()
    def get(self, request, user_id, family_id):
        family = self.get_family(family_id)
        if self.check_userid(family, user_id):
            serializer = FamilyDetailSerializer(instance=family)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema()
    def delete(self, request, user_id, family_id):
        family = self.get_family(family_id)
        if self.check_userid(family, user_id):
            family.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=FamilyUpdateSerializer)
    def patch(self, request, user_id, family_id):
        family = self.get_family(family_id)
        if self.check_userid(family, user_id):
            serializer = FamilyUpdateSerializer(instance=family, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)


@swagger_auto_schema(methods=['POST'])
@api_view(['POST'])
def cartoonize_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # print(settings.BASE_DIR)
    # print(user.child_image)
    
    profile_abs_path = user.child_image.path
    
    path = show_me_hat_and_face(profile_abs_path, user_id)
    result = {
        'path': path.split('back/')[1]
    }
    return Response(result, status=status.HTTP_200_OK)