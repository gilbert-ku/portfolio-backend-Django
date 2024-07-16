from rest_framework.views import APIView
from .serializer import ContactSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class IndexView(APIView):
    def get(self, request):
        return Response({"message": "welcome to first django api"})

class ContactView(APIView):
    # def get(self, request):
    #     pass


    def post(self, request):
        try:
            data = request.data

            serializer = ContactSerializer(data = data)

            if not serializer.is_valid():
                return Response({
                    "data" : serializer.errors,
                    "message" : "something went wrong"
                }, status =  status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({
                "data" : {},
                "message" : "Message Sent successfully"
            }, status =  status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({
                "data" : {},
                "message" : "something went wrong"
            }, status =  status.HTTP_400_BAD_REQUEST)

