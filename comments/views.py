from rest_framework.views import APIView
from .serializer import CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Comments

class CommentsView(APIView):
    def get(self, request, *args, **kwargs):
        try:

            uuid = kwargs.get("pk")


            if uuid:

                comment = Comments.objects.filter(uuid = uuid).first()

                if not comment:
                    return Response({
                        "Message" : "Invalid comment uuid"
                    }, status= status.HTTP_400_BAD_REQUEST)
                
                serializer = CommentSerializer(comment)

                return Response({
                    "comment": serializer.data,
                    "Message" : "Comment Fetched successfully"
                }, status= status.HTTP_200_OK)
            
            else:
                comments = Comments.objects.all()

                serializer = CommentSerializer(comments, many=True)

                return Response({
                    "comments" : serializer.data,
                    "Message" : "Comments fetched successfully"
                }, status= status.HTTP_200_OK)
            
        except Exception as e:
            print(e)
            return Response({
                "data": {},
                "message": "Something went wrong"
            }, status=status.HTTP_400_BAD_REQUEST)
            
            

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
        

    # delete
    def delete(self, request, *args, **kwargs):
        # try:

        #     comments = request.comments

        #     comment = Comments.objects.get(uuid = comments["uuid"])

        #     comment.delete()

        #     return Response({
        #         "Message" : "Comment was delete Successfully"
        #     }, status= status.HTTP_204_NO_CONTENT)
        
        # except Exception as e:
        #     return Response({
        #         "Message" : "Something went wrong"
        #     }, status= status.HTTP_400_BAD_REQUEST)

        try:

            # get uuid from Url kwargs
            uuid = kwargs.get("pk")

            comment = Comments.objects.filter(uuid=uuid).first()


            if not comment:
                return Response({
                    "Message" : "Invalid project uuid"
                }, status= status.HTTP_400_BAD_REQUEST)
            
            comment.delete()

            return Response({
                "Message": "Comment Was Delete Successfully"
            }, status= status.HTTP_204_NO_CONTENT)
        
        except Exception as e:
            print(e)
            return Response({
                "data": {},
                "message": "Something went wrong"
            }, status=status.HTTP_400_BAD_REQUEST)


