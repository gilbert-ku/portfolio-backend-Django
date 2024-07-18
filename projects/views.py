from rest_framework.views import APIView
from .serializer import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Projects

# Create your views here.

class ProjectsView(APIView):
    def get(self, request):
        return Response({"message": "welcome to first django api"})