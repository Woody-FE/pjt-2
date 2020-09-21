from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from .serializers import MyStorySerializer, StoryDetailSerializer, BranchDetailSerializer, SubstorySerializer, MyStoryCreateRequestSerializer, MyStoryCreateSerializer, MyCharacterSerializer, MyCharacterCreateSerializer, MyCharacterBasicSerializer
from .models import *


class APIViewWithAuthentication(APIView):
    permission_classes = (IsAuthenticated,)


class MyStoryView(APIViewWithAuthentication):
    
    def get(self, request):
        mystories = request.user.mystories
        serializer = MyStorySerializer(instance=mystories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=MyStoryCreateRequestSerializer)
    def post(self, request):
        user = request.user
        story_id = request.data.get('story_id')
        if not Story.objects.filter(id=story_id).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        story_name = request.data.get('story_name')

        data = {
           'story': story_id,
           'story_name': story_name,
           'user': user.id,
        }

        mystory = MyStoryCreateSerializer(data=data)

        if mystory.is_valid(raise_exception=True):
            instance = mystory.save()
            return Response(MyStorySerializer(instance=instance).data, status=status.HTTP_201_CREATED)


class MyStoryDetailView(APIViewWithAuthentication):

    def get_object(self, mystory_id):
        return get_object_or_404(MyStory, pk=mystory_id)

    def get(self, request, mystory_id):
        mystory = self.get_object(mystory_id)
        if request.user.id == mystory.user.id:
            serializer = MyStorySerializer(instance=mystory)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, mystory_id):
        mystory = self.get_object(mystory_id)
        mystory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StoryView(APIView):

    def get(self, request):
        stories = Story.objects.all()
        serializer = StoryDetailSerializer(instance=stories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StoryDetailView(APIViewWithAuthentication):

    def get_object(self, story_id):
        return get_object_or_404(Story, pk=story_id)

    def get(self, request, story_id):
        story = self.get_object(story_id)
        serializer = StoryDetailSerializer(instance=story)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BranchDetailView(APIViewWithAuthentication):

    def get(self, request, branch_id):
        branch = get_object_or_404(Branch, pk=branch_id)
        serializer = BranchDetailSerializer(instance=branch)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MyCharacterView(APIViewWithAuthentication):

    def get(self, request, mystory_id):
        mystory = get_object_or_404(MyStory, pk=mystory_id)
        serializer = MyCharacterSerializer(instance=mystory.mycharacters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=MyCharacterCreateSerializer)
    def post(self, request, mystory_id):
        serializer = MyCharacterCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            mystory = get_object_or_404(MyStory, pk=mystory_id)
            serializer.save(mystory=mystory)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class MyCharacterDetailView(APIViewWithAuthentication):
    
    def get_object(self, mycharacter_id):
        return get_object_or_404(MyCharacter, pk=MyCharacter_id)

    def get(self, request, mycharacter_id):
        character = self.get_object(mycharacter_id)
        serializer = MyCharacterSerializer(instance=character)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubstoryDetailView(APIViewWithAuthentication):

    def get(self, request, mystory_id, substory_id):
        mystory = get_object_or_404(MyStory, pk=mystory_id)
        substory = get_object_or_404(Substory, pk=substory_id)
        data = SubstorySerializer(instance=substory).data
        result = {**data}
        for value in data['scripts']:
            mycharacter = mystory.mycharacters.filter(mystory=mystory_id, character=value['character']['id'])
            if mycharacter:
                value['mycharacter'] = MyCharacterBasicSerializer(instance=mycharacter[0]).data
            else:
                value['mycharacter'] = {}
        return Response(result, status=status.HTTP_200_OK)


# 스토리 최종 만드는 로직 추가필요