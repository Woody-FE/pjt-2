from rest_framework import serializers

from .models import *


class StoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        depth = 1
        fields = '__all__'


class MyStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyStory
        depth = 1
        fields = (
            'id',
            'created',
            'story',
            'story_name',
            'mysubstory'
        )


class SubstorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Substory
        fields = '__all__'


class MySubstorySerializer(serializers.ModelSerializer):
    substory = SubstorySerializer()
    class Meta:
        model = MySubstory
        fields = '__all__'