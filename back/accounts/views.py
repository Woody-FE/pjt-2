from rest_framework.views import APIView
from rest_framework.parsers import FormParser

from .serializers import CreateUserSerializer


class CreateUserView(APIView):
    parser_classes = (FormParser, )
    serializer_class = CreateUserSerializer