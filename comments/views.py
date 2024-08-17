from rest_framework.views import APIView
from .serializer import CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Comments

class CommentsView(APIView):
    def get(self):
        pass

    def post(self, request):
        try:
            comments = request.comments

            serializer = CommentSerializer(comments = comments)

            if not serializer.is_valid():
                return Response({
                    "data" : serializer.errors,
                    "message" : "Something went wrong"
                }, status= status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({
                "message": "comment sent successfully"
            }, status= status.HTTP_201_CREATED)
        
        except Exception as e :
            return Response ({
                "Message" : "Something Went Wrong"
            }, status= status.HTTP_400_BAD_REQUEST)



