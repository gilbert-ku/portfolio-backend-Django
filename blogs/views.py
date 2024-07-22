from rest_framework.views import APIView
from .serializer import BlogSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Blogs

# Create your views here.


class BlogsIndex(APIView):
    def get(self, request):
        return Response({"message": "welcome to my blogs"})
    

class BlogView(APIView):

    def get(self, request):
        try:
            blogs = Blogs.objects.all()

            serializer = BlogSerializer(blogs, many = True)

            return Response({
                "data" : serializer.data,
                "message" : "Feedback fetch successfully"
            }, status =  status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({
                "data" : {},
                "message" : "something went wrong"
            }, status =  status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        try:
            data = request.data

            serializer = BlogSerializer(data= data)

            if not serializer.is_valid():
                return Response({
                    "data" : serializer.errors,
                    "message" : "something went wrong"
                }, status =  status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({
                "data" : {},
                "message" : "blog created successfully"
            }, status =  status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({
                "data" : {},
                "message" : "something went wrong"
            }, status =  status.HTTP_400_BAD_REQUEST)

           