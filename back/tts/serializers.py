from rest_framework import serializers


class TTSQuerySerializer(serializers.Serializer):
    numerator = serializers.IntegerField(required=False)
    denominator = serializers.IntegerField(required=False)