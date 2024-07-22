from rest_framework.views import APIView
from .serializer import BlogsSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Blogs

# Create your views here.


class BlogsIndex(APIView):
    def get(self, request):
        return Response({"message": "welcome to my blogs"})
