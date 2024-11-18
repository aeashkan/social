from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status

from .models import Post

class PostView(APIView):

    def get(self, request):
        pass

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


