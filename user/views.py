from rest_framework.views import APIView, Response
from rest_framework import status
from user.serializer import RegisterUserSeralizer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from user.models import User


class RegisterUserAPI(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        serializer = RegisterUserSeralizer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
        else:
            return Response({"result" : "error"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result" : {"user_id" : user.id}}, status=status.HTTP_200_OK)


class Users(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSeralizer
    queryset = User.objects.all()