from rest_framework.views import APIView
from .serializer import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Projects
import uuid

# Create your views here.

class ProjectIndex(APIView):
    def get(self, request):
        return Response({"message": "welcome to first django api"}) 
    
class ProjectsView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            uuid = kwargs.get('pk')  # Get UUID from URL kwargs

            if uuid:
                blog = Projects.objects.filter(uuid=uuid).first()

                if not blog:
                    return Response({
                        "data": {},
                        "message": "Invalid project uuid"
                    }, status=status.HTTP_400_BAD_REQUEST)

                serializer = ProjectSerializer(blog)
                return Response({
                    "data": serializer.data,
                    "message": "Project fetched successfully"
                }, status=status.HTTP_200_OK)
            else:
                blogs = Projects.objects.all()
                serializer = ProjectSerializer(blogs, many=True)
                return Response({
                    "data": serializer.data,
                    "message": "Projects fetched successfully"
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

            serializer = ProjectSerializer(data = data)

            if not serializer.is_valid():   
                return Response({
                    "data" : serializer.errors,
                    "message" : "something went wrong"
                }, status= status.HTTP_400_BAD_REQUEST)
            
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
        

    def patch(self, request, *args, **kwargs):

        try:
            uuid = kwargs.get('pk')  # Get UUID from URL kwargs

            # Use filter with .first() to handle DoesNotExist gracefully
            blog = Projects.objects.filter(uuid=uuid).first()  

            if not blog:
                return Response({
                    "data": {},
                    "message": "Invalid project uuid"
                }, status=status.HTTP_400_BAD_REQUEST)


            data = request.data

            serializer = ProjectSerializer(blog, data=data, partial = True)
            
            if serializer.is_valid():
                serializer.save()

                return Response({
                "data" : {},
                "message" : "Project was updated successfully"
            }, status =  status.HTTP_202_ACCEPTED)

        except Exception as e:
            print(e)
            return Response({
                "data" : {},
                "message" : "something went wrong"
            }, status =  status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        try:

            uuid = kwargs.get('pk') #get uuid from url kwargs

            # Use filter with .first() to handle DoesNotExist gracefully
            project = Projects.objects.filter(uuid=uuid).first()

            if not project:
                return Response({
                    "data" : {},
                    "message" : "Invalid project uuid"
                }, status= status.HTTP_400_BAD_REQUEST)


            project.delete()

            return Response({
                "message" : "Project was deleted successfully"
            }, status= status.HTTP_204_NO_CONTENT) 
        
        except Exception as e:
            print(e)
            return Response({
                "data" : {},
                "message" : "something went wrong"
            }, status =  status.HTTP_400_BAD_REQUEST)

