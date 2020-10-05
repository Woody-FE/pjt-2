from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

from stories.models import Script

from .tts import TTS
from accounts.models import CustomUser
from stories.models import Story
from .serializers import TTSQuerySerializer

import tossi

import os


User = settings.AUTH_USER_MODEL


@swagger_auto_schema(methods=['post'], query_serializer=TTSQuerySerializer)
@api_view(['POST'])
def create_voice(request, story_id, user_id):
    scripts = Script.objects.filter(has_name=False)
    user = get_object_or_404(CustomUser, pk=user_id)
    denominator = int(request.GET.get('denominator', None))
    numerator = int(request.GET.get('numerator', None))

    if denominator is None or numerator is None:
        length = scripts.count()
        div = length // denominator
        start = (numerator - 1) * div
        if denominator == numerator:
            scripts = scripts[start:]
        else:
            scripts = scripts[start: start + div]
    for script in scripts:
        s = script.content
        s = s.replace('<br>','.')

        splitted_string = s.split('{child_name}')
        wanted = splitted_string[1].split()[0].split('.')[0]

        temp = tossi.postfix(user.child_name, wanted)

        result_script = s.replace('{child_name}' + wanted, temp)
        
        store_path = f'{settings.BASE_DIR}/voice/story/{story_id}/user/{user_id}/'
        if not os.path.isdir(store_path):
            os.makedirs(store_path)
        
        TTS(result_script, f'{store_path}script_{script.id}.mp3')
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def create_narration(request, story_id):
    scripts = Script.objects.all()
    story = get_object_or_404(Story, pk=story_id)
    store_path = f'{settings.BASE_DIR}/voice/story/{story_id}/'
    for script in scripts:
        if script.character.id == 2 and '{child_name}' not in script.content:
            content = script.content.replace('<br>', '.')
            file_name = f'{store_path}script_{script.id}.mp3'
            if not os.path.isfile(file_name):
                TTS(content, file_name)
