from rest_framework.response import Response

from AI.texttospeech.samples.snippets.TTS import TTS

print(TTS('남북경협주 저가매수타이밍입니다. 주주님들 다들 화이팅합시다.', 'fighting.mp3'))