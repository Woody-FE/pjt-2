from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from .serializers import MyStorySerializer, StoryDetailSerializer, BranchDetailSerializer, SubstorySerializer
from .models import *


class APIViewWithAuthentication(APIView):
    permission_classes = (IsAuthenticated,)


class MyStoryView(APIViewWithAuthentication):
    
    def get(self, request):
        mystories = request.user.mystories
        serializer = MyStorySerializer(instance=mystories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # @swagger_auto_schema(request_body=)
    # def post(self, request):
        


class MyStoryDetailView(APIViewWithAuthentication):

    def get_object(self, mystory_id):
        return get_object_or_404(MyStory, pk=mystory_id)

    def get(self, request, mystory_id):
        mystory = self.get_object(mystory_id)
        if request.user.id == mystory.user.id:
            serializer = MyStorySerializer(instance=mystory)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)


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


class SubstoryDetailView(APIViewWithAuthentication):

    # substory 줄때 Mycharacter를 넣어서 줄 수 있는 방법???
    def get(self, request, substory_id):
        substory = get_object_or_404(Substory, pk=substory_id)
        serializer = SubstorySerializer(instance=substory)
        return Response(serializer.data, status=status.HTTP_200_OK)
    