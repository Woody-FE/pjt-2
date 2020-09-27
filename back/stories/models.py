from django.db import models
from django.conf import settings

from accounts.models import Family


User = settings.AUTH_USER_MODEL


class Substory(models.Model):
    back_image = models.ImageField(blank=True, null=True)
    next_id = models.IntegerField(blank=True, null=True)
    has_branch = models.BooleanField()
    story = models.ForeignKey('Story', on_delete=models.CASCADE, related_name='substories')


class StoryImage(models.Model):
    path = models.TextField()
    is_main_character = models.BooleanField(default=False)
    substory = models.ForeignKey(Substory, on_delete=models.CASCADE, related_name='images')


class Story(models.Model):
    name = models.CharField(max_length=20)
    cover_image = models.ImageField(null=True, blank=True)
    substory = models.ForeignKey(Substory, on_delete=models.CASCADE, related_name='original_story', null=True)


class Branch(models.Model):
    question = models.TextField()
    back_image = models.ImageField()
    story_id = models.IntegerField()
    left_image = models.ImageField(null=True)
    right_image = models.ImageField(null=True)


class Character(models.Model):
    name = models.CharField(max_length=20)
    thumbnail = models.ImageField(null=True, blank=True)
    family_ability = models.BooleanField()
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='characters')
    gender = models.CharField(max_length=2)


class MySubstory(models.Model):
    substory = models.ForeignKey(Substory, on_delete=models.CASCADE)
    next_id = models.IntegerField(blank=True, null=True)
    is_end = models.BooleanField()


class MyStory(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='mystories')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mystories')
    story_name = models.CharField(max_length=30)
    mystory = models.ForeignKey(MySubstory, on_delete=models.CASCADE, related_name='substories', null=True, blank=True)
    finished = models.BooleanField(default=False)
    

class MyCharacter(models.Model):
    mystory = models.ForeignKey(MyStory, on_delete=models.CASCADE, related_name='mycharacters')
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='mycharacters')
    family = models.ManyToManyField(Family, related_name='mycharacters')


class Script(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='scripts')
    order = models.IntegerField()
    content = models.TextField()
    substory = models.ForeignKey(Substory, on_delete=models.CASCADE, related_name='scripts')


class Select(models.Model):
    select = models.CharField(max_length=20)
    substory = models.ForeignKey(Substory, on_delete=models.CASCADE, related_name='selects')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='selects')
