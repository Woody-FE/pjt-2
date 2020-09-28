from django.conf import settings

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from stories.models import Script

from .tts import TTS


@api_view(['POST'])
def create_voice(request):
    scripts = Script.objects.all()
    for script in scripts:
        s = script.content
        s = s.replace('<br>','.')
        if not '{child_name}' in s and script.id > 51:
            TTS(s,f'{settings.BASE_DIR}/voice/story/1/script_{script.id}.mp3')
    
    return Response(status=status.HTTP_200_OK)