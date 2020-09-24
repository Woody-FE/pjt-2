import os.path

def TTS(sentence,output):
    from google.cloud import texttospeech

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=sentence)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR",
        name="ko-KR-Standard-A",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open(output, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file {}'.format(output))
    # [END tts_quickstart]
    
    return os.path.abspath(output)

path = TTS('남북경협주 저가매수타이밍입니다. 주주님들 다들 화이팅합시다.', 'fighting.mp3')
print(path)