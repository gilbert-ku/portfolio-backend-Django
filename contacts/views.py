from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class IndexView(APIView):
    def get(self, request):
        return Response({"message": "welcome to first django api"})
