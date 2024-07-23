from rest_framework.views import APIView
from .serializer import BlogSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Blogs

import uuid

# Create your views here.


class BlogsIndex(APIView):
    def get(self, request):
        return Response({"message": "welcome to my blogs"})
    

class BlogView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            uuid = kwargs.get('pk')  # Get UUID from URL kwargs

            if uuid:
                blog = Blogs.objects.filter(uuid=uuid).first()

                if not blog:
                    return Response({
                        "data": {},
                        "message": "Invalid project uuid"
                    }, status=status.HTTP_400_BAD_REQUEST)

                serializer = BlogSerializer(blog)
                return Response({
                    "data": serializer.data,
                    "message": "Blog fetched successfully"
                }, status=status.HTTP_200_OK)
            else:
                blogs = Blogs.objects.all()
                serializer = BlogSerializer(blogs, many=True)
                return Response({
                    "data": serializer.data,
                    "message": "Blogs fetched successfully"
                }, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                "data": {},
                "message": "Something went wrong"
            }, status=status.HTTP_400_BAD_REQUEST)


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
        

    def patch(self, request, *args, **kwargs):


        try:
            uuid = kwargs.get('pk')  # Get UUID from URL kwargs

            # Use filter with .first() to handle DoesNotExist gracefully
            blog = Blogs.objects.filter(uuid=uuid).first()  

            if not blog:
                return Response({
                    "data": {},
                    "message": "Invalid project uuid"
                }, status=status.HTTP_400_BAD_REQUEST)


            data = request.data

            serializer = BlogSerializer(blog, data=data, partial = True)
            
            if serializer.is_valid():
                serializer.save()

                return Response({
                "data" : {},
                "message" : "Blog was updated successfully"
            }, status =  status.HTTP_202_ACCEPTED)

        except Exception as e:
            print(e)
            return Response({
                "data" : {},
                "message" : "something went wrong"
            }, status =  status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, *args, **kwargs):
        try:
            uuid = kwargs.get('pk')  # Get UUID from URL kwargs

            # Use filter with .first() to handle DoesNotExist gracefully
            blog = Blogs.objects.filter(uuid=uuid).first()  

            if not blog:
                return Response({
                    "data": {},
                    "message": "Invalid project uuid"
                }, status=status.HTTP_400_BAD_REQUEST)

            blog.delete()

            return Response({
                "message": "Blog was deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            print(e)
            return Response({
                "data": {},
                "message": "Something went wrong"
            }, status=status.HTTP_400_BAD_REQUEST)

           