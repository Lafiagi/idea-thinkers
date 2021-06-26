from rest_framework.generics import  CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from authy.services import *
from .serializers import *
from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

class UserRegistrationView(CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = UserSerializer

    def post(self, request):
        data  = create_user(request)
        #there's an error return the error code
        if(len(data) == 2):
            msg,status = data
            return Response(msg , status = status)#not allowed

        token, first_name, last_name, email, phone_number = data
        return Response({'token':token,
                         'first_name': first_name,
                          "last_name":last_name,
                          "email":email,
                           "phone_number":phone_number,
                           },
                            status=200
                        )

class UserLoginView(CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = UserLoginSerializer
    authentication_classes = (TokenAuthentication,)
    def post(self, request):
        data, status  = login_user(request.data)
        return Response( data, status = status)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = (TokenAuthentication,)
    def get(self, request):
        msg = logout_user(request)
        return Response( msg , status = 200)


class WelcomeUserView(APIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = (TokenAuthentication,)
    def get(self, request):
        data  = welcome_user(request)
        return Response( data, status = status.HTTP_200_OK)
