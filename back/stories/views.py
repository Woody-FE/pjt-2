from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import MyStorySerializer


class MyStoryView(APIView):
    
    permission_classes = (IsAuthenticated, )
    
    def get(self, request):
        mystories = request.user.mystories
        serializer = MyStorySerializer(instance=mystories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # def post(self, request):
        