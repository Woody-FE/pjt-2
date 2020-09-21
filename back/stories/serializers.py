from rest_framework import serializers

from .models import *


class StoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
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


class MyStoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyStory
        fields = (
            'story',
            'story_name',
        )

        
class CharacterOfScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'id',
            'name',
            'thumbnail',
        )


class ScriptSerializer(serializers.ModelSerializer):
    character = CharacterOfScriptSerializer()
    class Meta:
        model = Script
        fields = (
            'id',
            'character',
            'order',
            'content',
            'substory',
        )


class SubstorySerializer(serializers.ModelSerializer):
    scripts = ScriptSerializer(many=True)
    class Meta:
        model = Substory
        fields = (
            'id',
            'next_id',
            'has_branch',
            'scripts',
            'images',
        )


class MySubstorySerializer(serializers.ModelSerializer):
    substory = SubstorySerializer()
    class Meta:
        model = MySubstory
        fields = '__all__'


class BranchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        depth = 1
        fields = (
            'id',
            'question',
            'back_image',
            'selects',
        )