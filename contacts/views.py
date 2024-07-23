from rest_framework.views import APIView
from .serializer import ContactSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Contacts

# Create your views here.

class IndexView(APIView):
    def get(self, request):
        return Response({"message": "welcome to first django api"})

class ContactView(APIView):
    # get
    def get(self, request):
        try:
            contacts = Contacts.objects.all()

            serializer = ContactSerializer(contacts, many = True)

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
        

# contact does not require pacth since it comes from client
    # def patch(self, request):
    #     try:
    #         data = request.data
    #         contact = Contacts.objects.get(id = data["id"])
    #         serializer = ContactSerializer(contact, data = data, partial = True)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response({
    #             "data" : {},
    #             "message" : "Message was updated successfully"
    #         }, status =  status.HTTP_202_ACCEPTED)
    #     except Exception as e:
    #         print(e)
    #         return Response({
    #             "data" : {},
    #             "message" : "something went wrong"
    #         }, status =  status.HTTP_400_BAD_REQUEST)
        


    def delete(self, request):
        try:
            data = request.data

            contact = Contacts.objects.get(id = data["id"])

            contact.delete()

            return Response({
                "message" : "Message was deleted successfully"
            }, status= status.HTTP_204_NO_CONTENT)
        
        except Exception as e:
            print(e)
            return Response({
                "data" : {},
                "message" : "something went wrong"
            }, status =  status.HTTP_400_BAD_REQUEST)



            
        
